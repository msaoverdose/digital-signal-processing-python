import librosa
import soundfile as sf
from scipy.signal import decimate, resample, resample_poly
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
0
file_path = '/home/msa/Desktop/sayısal.i.t/sound.mp3'
data, fs = librosa.load(file_path, sr=None, mono=True)  
print(f"Örnekleme frekansı: {fs}")
print(f"Toplam örnek sayısı: {len(data)}")

# 2. Ses Dalga Formunu Çizdirme
time = np.linspace(0, len(data) / fs, num=len(data))
plt.figure(figsize=(10, 4))
plt.plot(time, data)
plt.title("Orijinal Ses Dalga Formu")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")
plt.show()

# 3. Örnek Azaltma (Downsampling) - Örnek Sayısını Azaltma
M = 2  # Örnek azaltma faktörü
data_downsampled = decimate(data, M)
#sf.write("downsampled.wav", data_downsampled, fs)

# Yeni sesi dinleyin
print("Downsampled ses çalıyor...")
sd.play(data_downsampled, fs)
sd.wait()

# Çizdirme
time_downsampled = np.linspace(0, len(data_downsampled) / fs, num=len(data_downsampled))
plt.figure(figsize=(10, 4))
plt.plot(time_downsampled, data_downsampled)
plt.title("Örnek Sayısı Azaltılmış Ses Dalga Formu")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")
plt.show()

# 4. Örnekleme Frekansını Değiştirerek Örnek Azaltma
new_fs = fs // M
#sf.write("downsampled_freq.wav", data_downsampled, new_fs)

# Çizdirme
time_downsampled = np.linspace(0, len(data_downsampled) / new_fs, num=len(data_downsampled))
plt.figure(figsize=(10, 4))
plt.plot(time_downsampled, data_downsampled)
plt.title("Örnekleme Frekansı Azaltılmış Ses Dalga Formu")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")
plt.show()

# 5. Örnek Artırma (Upsampling) - Örnek Sayısını Artırma
L = 2  # Örnek artırma faktörü
data_upsampled = resample(data, len(data) * L)
#sf.write("upsampled.wav", data_upsampled, fs)

# Yeni sesi dinleyin
print("Upsampled ses çalıyor...")
sd.play(data_upsampled, fs)
sd.wait()

# Çizdirme
time_upsampled = np.linspace(0, len(data_upsampled) / fs, num=len(data_upsampled))
plt.figure(figsize=(10, 4))
plt.plot(time_upsampled, data_upsampled)
plt.title("Örnek Sayısı Artırılmış Ses Dalga Formu")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")
plt.show()

# 6. Örnekleme Frekansını Değiştirerek Örnek Artırma
new_fs = fs * L
#sf.write("upsampled_freq.wav", data_upsampled, new_fs)

# Çizdirme
time_upsampled = np.linspace(0, len(data_upsampled) / new_fs, num=len(data_upsampled))
plt.figure(figsize=(10, 4))
plt.plot(time_upsampled, data_upsampled)
plt.title("Örnekleme Frekansı Artırılmış Ses Dalga Formu")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")
plt.show()

# 7. Örnek Oranı Değişimi (Resampling) - M ve L ile
data_resampled = resample_poly(data, L, M)
new_fs_resample = fs * L // M
#sf.write("resampled.wav", data_resampled, new_fs_resample)

# Yeni sesi dinleyin
print("Resampled ses çalıyor...")
sd.play(data_resampled, new_fs_resample)
sd.wait()

# Çizdirme
time_resampled = np.linspace(0, len(data_resampled) / new_fs_resample, num=len(data_resampled))
plt.figure(figsize=(10, 4))
plt.plot(time_resampled, data_resampled)
plt.title("Örnek Oranı Değişmiş Ses Dalga Formu")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")
plt.show()

# Tek bir figürde tüm sinyalleri karşılaştırma
plt.figure(figsize=(12, 8))

# Orijinal Sinyal
plt.subplot(4, 1, 1)
plt.plot(time, data, color='blue')
plt.title("Orijinal Ses Dalga Formu")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")

# Örnek Sayısı Azaltılmış Sinyal (Downsampled)
M = 2  # Örnek azaltma faktörü
data_downsampled = decimate(data, M)
time_downsampled = np.linspace(0, len(data_downsampled) / fs, num=len(data_downsampled))
plt.subplot(4, 1, 2)
plt.plot(time_downsampled, data_downsampled, color='orange')
plt.title(f"Örnek Sayısı Azaltılmış (M={M})")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")

# Örnekleme Frekansı Azaltılmış Sinyal
new_fs_down = fs // M
plt.subplot(4, 1, 3)
plt.plot(time_downsampled, data_downsampled, color='green')
plt.title(f"Örnekleme Frekansı Azaltılmış (fs={new_fs_down} Hz)")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")

# Örnek Oranı Değiştirilmiş Sinyal (Resampled)
L = 2
data_resampled = resample_poly(data, L, M)
new_fs_resample = fs * L // M
time_resampled = np.linspace(0, len(data_resampled) / new_fs_resample, num=len(data_resampled))
plt.subplot(4, 1, 4)
plt.plot(time_resampled, data_resampled, color='red')
plt.title(f"Örnek Oranı Değişmiş (M={M}, L={L})")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Genlik")

# Tüm çizimleri göster
plt.tight_layout()
plt.show()
