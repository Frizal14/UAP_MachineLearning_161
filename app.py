import os
# ======================
# SETTING AWAL (WAJIB PALING ATAS)
# ======================
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import streamlit as st
import numpy as np
from PIL import Image
import pickle
import json
import pandas as pd
import plotly.express as px
import h5py
import time

# ======================
# IMPORT TENSORFLOW
# ======================
try:
    import tensorflow as tf
except ImportError:
    st.error("TensorFlow belum terinstall. Jalankan: pip install tensorflow")
    st.stop()

# ======================
# PATH CONFIG (VS CODE)
# ======================
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

PATH_MODEL_FINAL = os.path.join(BASE_PATH, "Model_Final")
PATH_MODEL_PRE = os.path.join(BASE_PATH, "Model_pre-trained")

MODEL_PATHS = {
    "Custom CNN": os.path.join(PATH_MODEL_FINAL, "fish_classifier_final.h5"),
    "VGG16 (Transfer Learning)": os.path.join(PATH_MODEL_PRE, "VGG16_fast_best_FIXED.keras"),
    "MobileNetV2 (Lightweight)": os.path.join(PATH_MODEL_PRE, "MobileNetV2_fast_best_FIXED.keras"),
}

LABEL_PATHS = {
    "cnn": os.path.join(PATH_MODEL_FINAL, "fish_labels_final.json"),
    "pretrained": os.path.join(PATH_MODEL_PRE, "class_names.pkl"),
}

st.set_page_config(
    page_title="Fish Classifier",
    page_icon="🐟",
    layout="wide"
)

# ======================
# CUSTOM CSS (DARK MODE)
# ======================
st.markdown("""
<style>
.sidebar-header {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
    margin-top: 10px;
    margin-bottom: 6px;
}

.sidebar-fish {
    font-size: 72px; /* ukuran emoji ikan */
    line-height: 1;
}

.sidebar-title {
    font-size: 28px;
    font-weight: 800;
    color: white;
    line-height: 1.1;
}
.sidebar-subtitle {
    text-align: center;
    font-size: 13px;
    color: #8b949e;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)


# ======================
# PATCH KERAS CONFIG (FIX SHAPE ERROR)
# ======================
def deep_clean_config(obj):
    """
    Patch AMAN untuk Keras 2.x - 3.x
    HANYA memodifikasi InputLayer
    """
    if isinstance(obj, dict):

        # Patch khusus InputLayer
        if obj.get("class_name") == "InputLayer":
            cfg = obj.get("config", {})
            if "shape" in cfg:
                cfg["batch_input_shape"] = cfg.pop("shape")
            obj["config"] = cfg

        # Patch dtype lama
        if "dtype" in obj and isinstance(obj["dtype"], dict):
            obj["dtype"] = obj["dtype"].get("config", {}).get("name", "float32")

        # Hapus metadata bermasalah
        obj.pop("registered_name", None)
        obj.pop("module", None)

        return {k: deep_clean_config(v) for k, v in obj.items()}

    elif isinstance(obj, list):
        return [deep_clean_config(i) for i in obj]

    return obj


def safe_load_model(path):
    """
    Loader model robust untuk .h5 lama
    """
    if not os.path.exists(path):
        return None

    # 1️⃣ Load normal
    try:
        return tf.keras.models.load_model(path, compile=False)
    except:
        pass

    # 2️⃣ Patch H5
    try:
        with h5py.File(path, "r+") as f:
            if "model_config" in f.attrs:
                raw = f.attrs["model_config"]
                if isinstance(raw, bytes):
                    raw = raw.decode("utf-8")

                cfg = json.loads(raw)
                cfg = deep_clean_config(cfg)
                f.attrs["model_config"] = json.dumps(cfg).encode("utf-8")

        return tf.keras.models.load_model(path, compile=False)

    except Exception as e:
        st.error(f"Gagal memuat {os.path.basename(path)}: {e}")
        return None

# ======================
# LOAD RESOURCE (CACHE)
# ======================
@st.cache_resource
def load_all_resources():
    progress = st.progress(0)
    status = st.empty()

    models = {}
    labels = {"cnn": [], "pretrained": []}

    # Load label
    status.text("📂 Memuat label...")
    if os.path.exists(LABEL_PATHS["cnn"]):
        with open(LABEL_PATHS["cnn"], "r") as f:
            labels["cnn"] = json.load(f)

    if os.path.exists(LABEL_PATHS["pretrained"]):
        with open(LABEL_PATHS["pretrained"], "rb") as f:
            labels["pretrained"] = pickle.load(f)

    progress.progress(25)

    # Load model
    for i, (name, path) in enumerate(MODEL_PATHS.items()):
        status.text(f"🧠 Memuat model: {name}")
        model = safe_load_model(path)
        if model:
            models[name] = model
        progress.progress(25 + int((i + 1) / len(MODEL_PATHS) * 75))
        time.sleep(0.3)

    status.empty()
    progress.empty()
    return models, labels


with st.spinner("Memuat model dan label..."):
    loaded_models, all_labels = load_all_resources()

# ======================
# SIDEBAR
# ======================
# ======================
# SIDEBAR (UPDATED HEADER)
# ======================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <div class="sidebar-fish">🐟</div>
        <div class="sidebar-title">Fish Classifier</div>
    </div>
    <div class="sidebar-subtitle">
        Made By Ferdy Rizal Mahendra Putra
        202210370311161
        Machine Learning C
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    if loaded_models:
        selected_models = st.multiselect(
            "Pilih model:",
            list(loaded_models.keys()),
            default=list(loaded_models.keys())
        )
    else:
        st.error("Model tidak ditemukan.")
        selected_models = []

    st.divider()
    st.write(f"**TensorFlow:** {tf.__version__}")


# ======================
# MAIN CONTENT
# ======================
st.title("🐟 Dashboard Klasifikasi Jenis Ikan")
st.info("**3 Model: CNN Non-Pretrained | VGG16 | MobileNetV2**")
st.markdown("---")

if not selected_models:
    st.warning("Pilih minimal satu model di sidebar.")
    st.stop()

uploaded_file = st.file_uploader(
    "Upload gambar ikan (JPG / PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🖼️ Gambar Input")
        st.image(img, use_container_width=True)

    with col2:
        st.subheader("📊 Hasil Prediksi")
        tabs = st.tabs(selected_models)
        summary = []

        for i, model_name in enumerate(selected_models):
            with tabs[i]:
                model = loaded_models[model_name]
                labels = all_labels["cnn"] if model_name == "Custom CNN" else all_labels["pretrained"]

                # Input size
                try:
                    h, w = model.input_shape[1], model.input_shape[2]
                except:
                    h, w = (224, 224)

                img_resized = img.resize((w, h))
                arr = tf.keras.preprocessing.image.img_to_array(img_resized)

                if model_name != "Custom CNN":
                    arr = arr / 255.0

                arr = np.expand_dims(arr, axis=0)

                preds = model.predict(arr, verbose=0)[0]
                probs = tf.nn.softmax(preds).numpy() if preds.max() > 1 else preds

                idx = np.argmax(probs)
                label = labels[idx] if idx < len(labels) else f"Class {idx}"
                conf = probs[idx]

                c1, c2 = st.columns(2)
                c1.metric("Prediksi", label)
                c2.metric("Confidence", f"{conf*100:.2f}%")

                df = pd.DataFrame({
                    "Label": labels,
                    "Probabilitas": probs
                }).sort_values("Probabilitas").tail(5)

                fig = px.bar(
                    df,
                    x="Probabilitas",
                    y="Label",
                    orientation="h",
                    color="Probabilitas",
                    color_continuous_scale="Blues"
                )
                fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="white")
                )
                st.plotly_chart(fig, use_container_width=True)

                summary.append({
                    "Model": model_name,
                    "Prediksi": label,
                    "Confidence": f"{conf*100:.2f}%"
                })

        st.divider()
        st.subheader("📝 Ringkasan Model")
        st.table(pd.DataFrame(summary))
