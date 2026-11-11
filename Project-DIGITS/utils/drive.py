from pathlib import Path
import gdown

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