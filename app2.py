from flask import Flask, request, jsonify
import joblib
import time
from datetime import datetime  
import os                     

app = Flask(__name__)
model = joblib.load('model_kelulusan.pkl')

LOG_FILE = 'log_prediksi.log'

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    data = request.json

    nama = data.get('Nama', 'Mahasiswa')
    ipk = data['IPK']
    kehadiran = data['Kehadiran']
    organisasi = data['Organisasi']

    features = [ipk, kehadiran, organisasi]
    prediction = model.predict([features])[0]
    elapsed_time = time.time() - start_time

    hasil = 'Lulus Tepat Waktu' if prediction == 1 else 'Tidak Lulus Tepat Waktu'
    predikat = 'Cumlaude' if (ipk >= 3.9 and prediction == 1) else 'Tidak Cumlaude'

    log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Prediksi | Nama: {nama}, IPK: {ipk}, Kehadiran: {kehadiran}, Organisasi: {organisasi}, Hasil: {hasil}, Predikat: {predikat}, Waktu: {elapsed_time:.4f}s\n"
    
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

    print(f"Prediction time: {elapsed_time:.4f} seconds")

    return jsonify({
        'Nama': nama,
        'Hasil': hasil,
        'Predikat': predikat,
        'Inference_time': elapsed_time
    })

if __name__ == '__main__':
    app.run(debug=True)
