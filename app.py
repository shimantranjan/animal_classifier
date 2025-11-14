# import streamlit as st
# import requests

# # FASTAPI BACKEND URL
# BACKEND_URL = "http://localhost:8000/predict/"   # change if deployed

# st.set_page_config(page_title="VetGuard AI", layout="centered")

# st.title("🐾 VetGuard AI — Animal Skin Disease Classifier")
# st.write("Upload an image and select the animal type to get predictions and medicine suggestions.")

# # Input: Animal Select
# animal_type = st.selectbox("Select Animal Type", ["dog", "cat", "cow"])

# # Input: Image uploader
# uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# # Predict Button
# if st.button("Predict"):
#     if uploaded_file is None:
#         st.error("Please upload an image first.")
#     else:
#         # Prepare request
#         files = {"file": uploaded_file.getvalue()}
#         data = {"animal_type": animal_type}

#         with st.spinner("Analyzing the image..."):
#             try:
#                 response = requests.post(BACKEND_URL, data=data, files=files)
#                 response.raise_for_status()  # raise error if status != 200
                
#                 result = response.json()

#                 # Output
#                 st.success("Prediction Successful!")
#                 st.subheader("🩺 Disease Prediction:")
#                 st.write(result.get("prediction", "No prediction returned"))

#                 st.subheader("💊 Medicine Suggestion:")
#                 st.write(result.get("medicine_suggestion", "No suggestion returned"))

#             except requests.exceptions.RequestException as e:
#                 st.error(f"Error connecting to backend: {e}")
import streamlit as st
import requests
from PIL import Image
import io

# FASTAPI BACKEND URL
BACKEND_URL = "http://localhost:8000/predict/"

# Page config
st.set_page_config(
    page_title="VetGuard AI",
    page_icon="🐾",
    layout="centered"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #eef2f3, #d9d9d9);
    }
    .card {
        background: rgba(255, 255, 255, 0.7);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(8px);
    }
    .center-text {
        text-align: center;
    }
    .upload-preview {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .stButton button {
        background: #4B9CD3;
        color: white !important;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: 0.2s;
    }
    .stButton button:hover {
        background: #2f7ebd;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("<h1 class='center-text'>🐾 VetGuard AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='center-text'>Smart Animal Skin Disease Classifier</h4>", unsafe_allow_html=True)
st.write("")

# Main card
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    animal_type = st.selectbox("Select Animal Type", ["dog", "cat", "cow"])

    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

    # 🌟 Show uploaded image preview
    if uploaded_file:
        st.markdown("<h5 class='center-text'>Uploaded Image Preview</h5>", unsafe_allow_html=True)
        img = Image.open(uploaded_file)
        st.image(img, use_column_width=True)

    # Predict Button
    if st.button("🔍 Analyze Skin Condition"):
        if uploaded_file is None:
            st.error("Please upload an image first.")
        else:
            files = {"file": uploaded_file.getvalue()}
            data = {"animal_type": animal_type}

            with st.spinner("🔬 Processing image & contacting VetGuard AI engine..."):
                try:
                    response = requests.post(BACKEND_URL, data=data, files=files)
                    response.raise_for_status()
                    result = response.json()

                    # Display results
                    st.success("🎉 Prediction Completed!")

                    st.subheader("🩺 Disease Prediction:")
                    st.info(result.get("prediction", "No prediction returned"))

                    st.subheader("💊 Medicine Suggestion:")
                    st.success(result.get("medicine_suggestion", "No suggestion returned"))

                except requests.exceptions.RequestException as e:
                    st.error(f"⚠ Error connecting to backend: {e}")

    st.markdown("</div>", unsafe_allow_html=True)
