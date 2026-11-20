# Image Steganography

A simple and interactive web application built with Streamlit that allows users to hide and extract secret text messages, files, and images inside another image using the **Least Significant Bit (LSB)** technique.

## 🚀 Features

- Hide **text messages** inside images.
- Hide **different types of files** inside images, including documents, executables, and images.
- Extract hidden content from steganographic images.
- Download the encoded (stego) image containing hidden data.
- Supports multiple image formats: `PNG`, `JPG`, `JPEG`, and `BMP`.
- User-friendly **Streamlit interface** with separate tabs for encoding and decoding.
- Encryption layer using Fernet for additional data security.

## 📂 Project Structure

```text
Image_Steganography/
│
├── Steganography_Logic/
│   ├── least_significant_bit.py
│   ├── filetobyte_conversion.py
│   ├── validators_check.py
│   └── crypto_security_layer.py
│
├── main.py
├── Streamlit_UI.py
├── requirements.txt
├── README.md
└── LICENSE
```

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Abhishek-Sahu11/Image_Steganography.git

cd Image_Steganography
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

**Activate the virtual environment:**

Windows:
```bash
.venv\Scripts\activate
```

Linux / macOS:
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run main.py
```

Once executed, Streamlit will start the application and provide a local URL that you can open in your browser.

## 📸 Usage

### 🔐 Encoding

1. Upload a cover image.
2. Choose the data type (Text or File).
3. Enter your secret message or upload a file.
4. Click the **Encode** button.
5. Download the generated stego image.

### 🔎 Decoding

1. Upload the stego image.
2. Click the **Decode** button.
3. Extract the hidden content.
4. View the extracted text or download the extracted file.

## 📌 Future Improvements

- Support for audio and video steganography.
- Password-protected encoding and decoding.
- Export operation logs and reports.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
