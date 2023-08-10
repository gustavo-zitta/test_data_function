import os

try:
    import requests
except ImportError:
    print("Missing 'requests' library. Installing...")
    os.system('pip install requests')
    import requests

try:
    import zipfile
except ImportError:
    print("Missing 'zipfile' library. Installing...")
    os.system('pip install zipfile')
    import zipfile

try:
    from pathlib import Path
except ImportError:
    print("Missing 'pathlib' library. Installing...")
    os.system('pip install pathlib')
    from pathlib import Path

def download_data(source: str,
                  destination: str,
                  remove_source: bool = True) -> Path:
    """Downloads a zipped dataset from source and unzips to destination.
    ... (rest of your docstring) ...
    """
    # Setup path to data folder
    data_path = Path("data/")
    image_path = data_path / destination

    # If the image folder doesn't exist, download it and prepare it...
    if image_path.is_dir():
        print(f"[INFO] {image_path} directory exists, skipping download.")
    else:
        print(f"[INFO] Did not find {image_path} directory, creating one...")
        image_path.mkdir(parents=True, exist_ok=True)

        # Download data
        target_file = Path(source).name
        with open(data_path / target_file, "wb") as f:
            request = requests.get(source)
            print(f"[INFO] Downloading {target_file} from {source} to {data_path}...")
            f.write(request.content)

        # Unzip DATA
        with zipfile.ZipFile(data_path / target_file, "r") as zip_ref:
            print(f"[INFO] Unzipping {target_file} data to {image_path}...")
            zip_ref.extractall(image_path)

        # Remove .zip file
        if remove_source:
            os.remove(data_path / target_file)

    return image_path

# Example usage
download_data(source="https://github.com/gustavo-zitta/ML-algorithms-/archive/refs/heads/main.zip",
              destination="data_from_github")
