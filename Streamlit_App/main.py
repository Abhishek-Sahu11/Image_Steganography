import sys
import os

# Add repo root to Python path (must be first!)
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

import streamlit as st
from Steganography_Logic.least_significant_bit import encode, decode
from Steganography_Logic.filetobyte_conversion import file_to_bytes, bytes_to_file
from Steganography_Logic.validators_check import max_capacity, check_capacity
from Streamlit_UI import upload_image, upload_file
from io import BytesIO



st.title("🐺 Image Steganography App")
st.write("Hide text or files inside images, and extract them back.")

tab1, tab2 = st.tabs(["🔐 Encode", "🔎 Decode"])

# -----------------------
# Encode Tab
# -----------------------
with tab1:
    st.subheader("Encode Data into Image")

    cover_image = upload_image("Upload Cover Image")
    data_choice = st.radio("What do you want to hide?", ["Text", "File"])

    if cover_image:
        if data_choice == "Text":
            text = st.text_area("Enter text to hide")
            if st.button("Encode Text"):
                if check_capacity(cover_image, text.encode()):
                    stego = encode(cover_image, text.encode())
                    st.image(stego, caption="Stego Image Preview")

                    # Save image correctly to buffer for download
                    buf = BytesIO()
                    stego.save(buf, format="PNG")
                    st.download_button("Download Stego Image", buf.getvalue(), "stego.png")

                else:
                    st.error("Image is too small to hold this text!")
        else:
            file_bytes, filename = upload_file("Upload a File to hide")
            if file_bytes and st.button("Encode File"):
                if check_capacity(cover_image, file_bytes):
                    stego = encode(cover_image, file_bytes)
                    st.image(stego, caption="Stego Image Preview")

                    buf = BytesIO()
                    stego.save(buf, format="PNG")
                    st.download_button("Download Stego Image", buf.getvalue(), "stego.png")
                else:
                    st.error("Image is too small to hold this file!")

# -----------------------
# Decode Tab
# -----------------------
with tab2:
    st.subheader("Decode Data from Image")

    stego_image = upload_image("Upload Stego Image")
    if stego_image and st.button("Decode"):
        hidden_data = decode(stego_image)

        if hidden_data:
            try:
                # Try decoding as text
                decoded_text = hidden_data.decode()
                st.success("Hidden text found:")
                st.code(decoded_text)
            except UnicodeDecodeError:
                # Try opening as image
                from PIL import Image
                import io

                try:
                    hidden_img = Image.open(io.BytesIO(hidden_data))
                    st.success("Hidden image found:")
                    st.image(hidden_img, caption="Decoded Hidden Image")
                    st.download_button(
                        "Download Hidden Image",
                        hidden_data,
                        "hidden_output.png",
                        mime="image/png"
                    )
                except Exception:
                    # Fallback: binary file
                    st.success("Hidden file found!")
                    st.download_button(
                        "Download Hidden File",
                        hidden_data,
                        "hidden_output.bin"
                    )
        else:
            st.error("No hidden data found in image.")


