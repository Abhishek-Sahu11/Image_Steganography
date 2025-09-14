
def file_to_bytes(file_path: str) -> bytes:
    #Read a file and return its contents as bytes
    with open(file_path, "rb") as f:
        return f.read()


def bytes_to_file(data: bytes, output_path: str) -> None:
    #Write bytes to a file
    with open(output_path, "wb") as f:
        f.write(data)
