from pathlib import Path

def main():
    project_dir = Path(__file__).resolve().parents[1]
    dataset_file = project_dir / "dataset" / "data.yaml"

    print("PJ1 - Computer Vision and Deep Learning")
    print(f"Folder project : {project_dir}")
    print(f"Konfigurasi    : {dataset_file}")
    print(f"File dataset tersedia: {dataset_file.exists()}")

    if not dataset_file.exists():
        print("Periksa kembali lokasi dataset/data.yaml.")
        return

    print("Pemeriksaan awal selesai.")
    print("Dataset dan instruksi eksperimen perlu dipastikan sebelum training.")

if __name__ == "__main__":
    main()