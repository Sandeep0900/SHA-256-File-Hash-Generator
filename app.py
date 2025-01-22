import streamlit as st
import hashlib

def hash_file(file):
    """
    Function to hash a file using SHA-256.
    Args:
        file: File object to be hashed.
    Returns:
        str: The hexadecimal hash of the file.
    """
    sha256_hash = hashlib.sha256()
    for chunk in iter(lambda: file.read(4096), b""):
        sha256_hash.update(chunk)
    file.seek(0)  # Reset file pointer after reading
    return sha256_hash.hexdigest()

# Streamlit App
st.title("SHA-256 File Hash Generator")
st.write("Upload a file below to generate its SHA-256 hash.")

# File uploader section
uploaded_file = st.file_uploader("Upload your file", type=None)  # Accepts all file types

# Process uploaded file
if uploaded_file is not None:
    st.write(f"**File uploaded:** `{uploaded_file.name}`")
    # Compute hash
    file_hash = hash_file(uploaded_file)
    st.write("### File Hash:")
    st.code(file_hash, language="plaintext")
else:
    st.info("Please upload a file to generate its hash.")
