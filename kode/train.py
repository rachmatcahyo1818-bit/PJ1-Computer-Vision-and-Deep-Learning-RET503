
import argparse
from pathlib import Path

from ultralytics import YOLO


def main():
    root = Path(__file__).resolve().parents[1]

    parser = argparse.ArgumentParser(description="Training YOLO11 untuk deteksi APD")
    parser.add_argument("--data", default=str(root / "dataset" / "data.yaml"))
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--batch", type=int, default=8)
    parser.add_argument("--name", default="ppe_k3")
    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.is_absolute():
        data_path = root / data_path

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset YAML tidak ditemukan: {data_path}")

    model = YOLO(args.model)
    results = model.train(
        data=str(data_path),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        patience=25,
        project=str(root / "hasil"),
        name=args.name,
    )

    print(f"\nTraining selesai. Hasil tersimpan di: {results.save_dir}")


if __name__ == "__main__":
    main()
