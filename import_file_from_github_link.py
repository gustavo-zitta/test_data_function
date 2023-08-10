import os

try:
    import requests
except ImportError:
    print("Missing 'requests' library. Installing...")
    os.system('pip install requests')
    import requests

try:
    from pathlib import Path
except ImportError:
    print("Missing 'pathlib' library. Installing...")
    os.system('pip install pathlib')
    from pathlib import Path

def download_file(source: str,
                  destination: str,
                  remove_source: bool = True) -> Path:
    """Downloads a file from source and saves it to destination.
    ... (rest of your docstring) ...
    """
    # Setup path to data folder
    data_path = Path("data/")
    file_path = data_path / destination

    # If the file doesn't exist, download it...
    if file_path.exists():
        print(f"[INFO] {file_path} already exists, skipping download.")
    else:
        print(f"[INFO] Did not find {file_path}, downloading...")
        data_path.mkdir(parents=True, exist_ok=True)

        # Download data
        response = requests.get(source)
        with open(file_path, "wb") as f:
            print(f"[INFO] Downloading file from {source} to {file_path}...")
            f.write(response.content)

        print(f"[INFO] Download completed.")

        # Remove the source file
        if remove_source:
            print(f"[INFO] Removing the source file: {source}")
            os.remove(file_path)

    return file_path

# Example usage
download_file(source="https://example.com/yourfile.ext",
              destination="yourfile.ext")
