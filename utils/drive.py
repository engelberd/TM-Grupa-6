from pathlib import Path
import gdown

def download_data(url, data_dir="data"):
    data_dir = Path(data_dir)

    gdown.download_folder(
        url=url,
        output=str(data_dir),
        quiet=True
    )

    print("Pliki:", [p.name for p in data_dir.iterdir() if p.is_file() and p.name != ".gitkeep"])

    return data_dir