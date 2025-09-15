import streamlit as st
from PIL import Image


def upload_image(label="Upload an Image"):
    #Streamlit file uploader for images
    uploaded_file = st.file_uploader(label, type=["png", "jpg", "jpeg", "bmp"])
    if uploaded_file:
        return Image.open(uploaded_file).convert("RGB")
    return None


def upload_file(label="Upload a File"):
    #Streamlit file uploader for generic files
    uploaded_file = st.file_uploader(label, type=None)
    if uploaded_file:
        return uploaded_file.read(), uploaded_file.name
    return None, None
