from cryptography.fernet import Fernet


def generate_key(password: str) -> bytes:
    
    # Placeholder: not password-based for simplicity
    return Fernet.generate_key()  

def encrypt(data: bytes, key: bytes) -> bytes:
    #Encrypt data using Fernet key
    fernet = Fernet(key)
    return fernet.encrypt(data)


def decrypt(data: bytes, key: bytes) -> bytes:
    #Decrypt data using Fernet key
    fernet = Fernet(key)
    return fernet.decrypt(data)
