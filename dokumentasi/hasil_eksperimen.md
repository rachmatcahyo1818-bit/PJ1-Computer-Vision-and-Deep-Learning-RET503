# Hasil Eksperimen YOLO11n

## Konfigurasi
- Model: YOLO11n
- Epoch: 30
- Ukuran gambar: 640
- Batch size: 8
- Dataset: 200 gambar (140 train, 40 validation, 20 test)
- Kelas berlabel: mask dan glasses

## Hasil evaluasi pada data test

| Metrik | Hasil |
|---|---:|
| Precision | 96.68% |
| Recall | 100% |
| mAP50 | 99.50% |
| mAP50-95 | 80.66% |
| Waktu inferensi rata-rata | 38.5 ms/gambar |

## Hasil per kelas

| Kelas | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| Mask | 96.0% | 100% | 99.5% | 83.3% |
| Glasses | 97.4% | 100% | 99.5% | 78.0% |

## Catatan
Dataset yang digunakan memiliki dua kelas berlabel, yaitu mask dan glasses.
Deteksi gloves belum dapat dievaluasi karena tidak ditemukan label kelas tersebut.
Hasil ini berasal dari pengujian 20 gambar dan belum mewakili seluruh kondisi penggunaan nyata.

## Lokasi hasil
- Model terbaik: hasil/ppe_k3-3/weights/best.pt
- Gambar hasil prediksi: runs/detect/hasil/uji_test
- Grafik evaluasi: runs/detect/hasil/evaluasi_test
