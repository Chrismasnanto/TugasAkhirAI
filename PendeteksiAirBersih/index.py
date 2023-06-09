import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB


class AirBersih:
    # Class untuk mendeteksi kualitas air bersih
    def __init__(self, pH, suhu, kekeruhan, kandungan_logam):
        self.pH = pH
        self.suhu = suhu
        self.kekeruhan = kekeruhan
        self.kandungan_logam = kandungan_logam

    # Method untuk mengecek kualitas air
    def cek_pH(self):
        if 6.5 <= self.pH <= 8.5:
            return "pH: {:.2f} (Normal)".format(self.pH)
        else:
            return "pH: {:.2f} (Tercemar)".format(self.pH)

    # Method untuk mengecek kualitas air
    def cek_suhu(self):
        if 25 <= self.suhu <= 40:
            return "Suhu: {:.2f} derajat Celsius (Normal)".format(self.suhu)
        else:
            return "Suhu: {:.2f} derajat Celsius (Tercemar)".format(self.suhu)

    def cek_kekeruhan(self):
        if self.kekeruhan < 5:
            return "Kekeruhan: {:.2f} NTU (Normal)".format(self.kekeruhan)
        else:
            return "Kekeruhan: {:.2f} NTU (Tercemar)".format(self.kekeruhan)

    def cek_kandungan_logam(self):
        if self.kandungan_logam < 0.5:
            return "Kandungan Logam: {:.2f} ppm (Normal)".format(self.kandungan_logam)
        else:
            return "Kandungan Logam: {:.2f} ppm (Tercemar)".format(self.kandungan_logam)

    def air_dapat_digunakan(self):
        if (6.5 <= self.pH <= 8.5) and (25 <= self.suhu <= 40) and (self.kekeruhan < 5) and (
                self.kandungan_logam < 0.5):
            return "Air dapat digunakan."
        else:
            return "Air tidak dapat digunakan."


def input_data_air():
    try:
        pH = float(input("Masukkan nilai pH air: "))
        suhu = float(input("Masukkan suhu air (derajat Celsius): "))
        kekeruhan = float(input("Masukkan kekeruhan air (NTU): "))
        kandungan_logam = float(input("Masukkan kandungan logam air (ppm): "))
        return AirBersih(pH, suhu, kekeruhan, kandungan_logam)
    except ValueError:
        print("Input tidak valid. Mohon masukkan angka.")
        return input_data_air()


def main():
    print("Program Pendeteksi Air Bersih")
    print("========================")
    print()

    air_sampel = input_data_air()
    print()
    print("=== Data Air ===")
    print(air_sampel.cek_pH())
    print(air_sampel.cek_suhu())
    print(air_sampel.cek_kekeruhan())
    print(air_sampel.cek_kandungan_logam())
    print()

    # Menyimpan data ke dalam file CSV
    with open('data_air.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([air_sampel.pH, air_sampel.suhu, air_sampel.kekeruhan, air_sampel.kandungan_logam])

    # Menampilkan data dalam bentuk grafik batang
    labels = ['pH', 'Suhu', 'Kekeruhan', 'Kandungan Logam']
    data = [air_sampel.pH, air_sampel.suhu, air_sampel.kekeruhan, air_sampel.kandungan_logam]

    # Mendefinisikan kelas Bayes
    class Bayes:
        def __init__(self, data):
            self.data = data

        def train(self, X, y):
            self.model = GaussianNB()
            self.model.fit(X, y)

        def predict(self, X):
            return self.model.predict(X)

    # Data training untuk klasifikasi air dapat digunakan atau tidak
    X_train = np.array([[6.5, 25, 4, 0.4], [8, 30, 3, 0.3], [7, 35, 2, 0.2], [7.2, 28, 3.5, 0.1]])
    y_train = np.array(['Dapat digunakan', 'Dapat digunakan', 'Tidak Dapat digunakan', 'Tidak Dapat digunakan'])

    # Membuat objek Bayes
    bayes = Bayes(air_sampel)

    # Melatih model
    bayes.train(X_train, y_train)

    # Menghasilkan prediksi
    X_test = np.array([[air_sampel.pH, air_sampel.suhu, air_sampel.kekeruhan, air_sampel.kandungan_logam]])
    prediction = bayes.predict(X_test)

    # Menampilkan hasil prediksi
    if prediction == 'Dapat digunakan':
        print("Prediksi: Air dapat digunakan.")
    else:
        print("Prediksi: Air tidak dapat digunakan.")

    plt.bar(labels, data)
    plt.title("Data Kualitas Air")
    plt.xlabel("Parameter")
    plt.ylabel("Nilai")
    plt.show()

if __name__ == '__main__':
    main()
