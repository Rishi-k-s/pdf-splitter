def remove_null_bytes(filename):
    with open(filename, 'rb') as f:
        content = f.read()

    cleaned_content = content.replace(b'\x00', b'')

    with open(filename, 'wb') as f:
        f.write(cleaned_content)

# Replace these paths with the correct paths to your files
remove_null_bytes('F:\\dev\\pdf_splitter\\main.py')
remove_null_bytes('F:\\dev\\pdf_splitter\\test.py')
