from pathlib import Path
import argparse
from ultralytics import YOLO


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT / "hasil" / "ppe_k3-3" / "weights" / "best.pt"


def main():
    parser = argparse.ArgumentParser(
        description="Prediksi deteksi APD menggunakan YOLO11"
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Path gambar/video atau nomor kamera, misalnya 0",
    )
    parser.add_argument(
        "--model",
        default=str(DEFAULT_MODEL),
        help="Path model .pt",
    )
    parser.add_argument("--conf", type=float, default=0.25)
    args = parser.parse_args()

    model_path = Path(args.model)
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model tidak ditemukan: {model_path}\n"
            "Pastikan file best.pt tersedia di folder hasil training."
        )

    model = YOLO(str(model_path))
    source = int(args.source) if args.source.isdigit() else args.source

    model.predict(
        source=source,
        conf=args.conf,
        show=True,
        save=True,
    )


if __name__ == "__main__":
    main()