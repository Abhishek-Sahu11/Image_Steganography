## Image_Stegonography

A simple and interactive web app built with Streamlit that lets you hide and extract secret text, files, or images inside another image using the Least Significant Bit (LSB) technique.

## 🚀 Features

- Hide **text messages** inside images.
- Hide **any type of file** inside images (documents, executables, images, etc.).
- Extract hidden content from stego images.
- Download the encoded (stego) image with hidden data.
- Supports multiple image formats: `PNG, JPG, JPEG, BMP`.
- User-friendly **Streamlit UI** with tabs for encoding and decoding.

## 📂 Project Structure

Image_Steganography/
│── Steganography_Logic/
│ ├── least_significant_bit.py # Core LSB encode/decode functions
│ ├── filetobyte_conversion.py # File ↔ bytes conversion helpers
│ ├── validators_check.py # Capacity check utilities
│ ├── crypto_security_layer.py # Encryption layer with Fernet
│
│
│ ├── main.py # Streamlit entry point
│
│── Streamlit_UI.py # UI helpers (file/image uploaders)
│── requirements.txt
│── README.md


## 🛠️ Installation & Setup

1. Clone the repository
     ```bash
     git clone https://github.com/<your-username>/Image_Steganography.git
     cd Image_Steganography


## Create a virtual environment (recommended)

     python -m venv venv        # Use Python -m venv .venv (to hide venv file)
     source venv/bin/activate   # On Linux/Mac
     venv\Scripts\activate.bat     # On Windows


## Install dependencies

     pip install -r requirements.txt


## Run the app

     streamlit run app/main.py (without venv)
     python -m streamlit run Streamlit_App/main.py (with venv)
     or
     # main.py and Streamlit_UI.py has been kept out of the folder due to deployment issues 
     python -m streamit run main.py (With venv)


## 📸 Usage

     🔐 Encode

         Upload a cover image.

         Choose Text or File as the data type.

         Enter text / upload a file.

         Click Encode.

         Download the Stego Image.

     🔎 Decode

         Upload a stego image.

         Click Decode.

         Extracted data will be shown as text, image, or file.


## 📌 Future Improvements

      Support for audio/video steganography 🎵🎥

      Add password-protected encoding/decoding 🔑

      Export operation logs/reports 📄



## 📜 License

     This project is licensed under the MIT License – see the LICENSE







