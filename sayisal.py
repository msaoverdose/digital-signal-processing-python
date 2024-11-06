import librosa
import soundfile as sf
from scipy.signal import decimate, resample, resample_poly
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

dosya_yolu = '/home/msa/Desktop/sayısal.i.t/digital-signal-processing-python/sound.mp3'
veri, fs = librosa.load(dosya_yolu, sr=None, mono=True)

def orijinal_ses():
    print("Orijinal ses çalıyor...")
    sd.play(veri, fs)
    sd.wait()
    print(f"Örnekleme frekansı: {fs}")
    print(f"Toplam örnek sayısı: {len(veri)}")
    zaman = np.linspace(0, len(veri) / fs, num=len(veri))
    plt.figure(figsize=(10, 4))
    plt.plot(zaman, veri)
    plt.title(f"Orijinal Ses Dalga Formu (Örnek Sayısı: {len(veri)})")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

def azaltma():
    M = 2
    azaltılmış_veri = decimate(veri, M)
    sd.play(azaltılmış_veri, fs // M)
    sd.wait()
    zaman_azaltılmış = np.linspace(0, len(azaltılmış_veri) / (fs // M), num=len(azaltılmış_veri))
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_azaltılmış, azaltılmış_veri)
    plt.title(f"Örnek Sayısı Azaltılmış Ses Dalga Formu (Örnek Sayısı: {len(azaltılmış_veri)})")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

def M_ile_azaltılmış():
    M = 2
    azaltılmış_veri = decimate(veri, M)
    yeni_fs = fs // M
    zaman_azaltılmış = np.linspace(0, len(azaltılmış_veri) / yeni_fs, num=len(azaltılmış_veri))
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_azaltılmış, azaltılmış_veri)
    plt.title(f"Örnekleme Frekansı Azaltılmış Ses Dalga Formu (Örnek Sayısı: {len(azaltılmış_veri)})")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

def ornek_arttırma():
    L = 2
    artırılmış_veri = resample(veri, len(veri) * L)
    print("Örnek artırılmış ses çalıyor...")
    sd.play(artırılmış_veri, fs)
    sd.wait()
    zaman_artırılmış = np.linspace(0, len(artırılmış_veri) / fs, num=len(artırılmış_veri))
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_artırılmış, artırılmış_veri)
    plt.title(f"Örnek Sayısı Artırılmış Ses Dalga Formu (Örnek Sayısı: {len(artırılmış_veri)})")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

def L_ile_ornek():
    L = 2
    artırılmış_veri = resample(veri, len(veri) * L)
    yeni_fs = fs * L
    zaman_artırılmış = np.linspace(0, len(artırılmış_veri) / yeni_fs, num=len(artırılmış_veri))
    sd.play(artırılmış_veri, yeni_fs)
    sd.wait()
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_artırılmış, artırılmış_veri)
    plt.title(f"Örnekleme Frekansı Artırılmış Ses Dalga Formu (Örnek Sayısı: {len(artırılmış_veri)})")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()
def hepsi_tek_grafikte():
    plt.figure(figsize=(12, 8))
    plt.subplot(4, 1, 1)
    plt.plot(time, data, color='blue')
    plt.title("Orijinal Ses Dalga Formu")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")

    M = 2  
    data_downsampled = decimate(data, M)
    time_downsampled = np.linspace(0, len(data_downsampled) / fs, num=len(data_downsampled))
    plt.subplot(4, 1, 2)
    plt.plot(time_downsampled, data_downsampled, color='orange')
    plt.title(f"Örnek Sayısı Azaltılmış (M={M})")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")


    new_fs_down = fs // M
    plt.subplot(4, 1, 3)
    plt.plot(time_downsampled, data_downsampled, color='green')
    plt.title(f"Örnekleme Frekansı Azaltılmış (fs={new_fs_down} Hz)")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")


    L = 2
    data_resampled = resample_poly(data, L, M)
    new_fs_resample = fs * L // M
    time_resampled = np.linspace(0, len(data_resampled) / new_fs_resample, num=len(data_resampled))
    plt.subplot(4, 1, 4)
    plt.plot(time_resampled, data_resampled, color='red')
    plt.title(f"Örnek Oranı Değişmiş (M={M}, L={L})")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")


    plt.tight_layout()
    plt.show()    

while True:
    print("1) Orjinal Sesin Grafiğini çiz ve oynat\n"
          "2) Örnek Azaltılmış Sesin Grafiğini çiz ve oynat\n"
          "3) Örneği M ile azaltılmış Grafiğini çiz ve oynat\n"
          "4) Örnekleme frekansını değiştirmeden L ile örnek artırılmış Grafiğini çiz ve oynat\n"
          "5) L ile Artırılmış Sesin Grafiğini çiz ve oynat\n"
          "6) Tüm grafikleri yanyana göster\n"
          "Diger) Çıkış \n")
    
    sayi = input("Çalıştırmak istediğiniz program: ")

    if sayi == '1':
        orijinal_ses()
    elif sayi == '2':
        azaltma()
    elif sayi == '3':
        M_ile_azaltılmış()
    elif sayi == '4':
        ornek_arttırma()
    elif sayi == '5':
        L_ile_ornek()
    elif sayi == '6':
        hepsi_tek_grafikte()    
    else:
        break



