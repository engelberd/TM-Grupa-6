from pathlib import Path
import gdown
from zipfile import ZipFile

def download_data(url, data_dir="data"):
    data_dir = Path(data_dir)

    files = gdown.download_folder(
        url=url,
        output=str(data_dir),
        quiet=True,
        resume=True,
    )

    print(f"Plików: {len(files)}")

    return data_dir

def download_zip(zip_url, extract_dir="data"):
    data_dir = Path(extract_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    zip_path = data_dir / "digits.zip"

    if gdown.download(zip_url, str(zip_path), quiet=False) is None:
        raise RuntimeError("Nie udało się pobrać ZIP-a.")

    with ZipFile(zip_path) as archive:
        archive.extractall(data_dir)

    zip_path.unlink()
    return data_dir