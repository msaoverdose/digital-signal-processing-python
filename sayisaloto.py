import librosa
import soundfile as sf
from scipy.signal import decimate, resample, resample_poly
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
dosya_yolu = '/home/msa/Desktop/sayısal.i.t/digital-signal-processing-python/sound.mp3'
data, fs = librosa.load(dosya_yolu, sr=None, mono=True)  
def orijinal_ses():
      print("Orijinal ses çalıyor...")
      sd.play(data, fs)
      sd.wait()

      print(f"Örnekleme frekansı: {fs}")
      print(f"Toplam örnek sayısı: {len(data)}")
      time = np.linspace(0, len(data) / fs, num=len(data))
      plt.figure(figsize=(10, 4))
      plt.plot(time, data)
      plt.title("Orijinal Ses Dalga Formu")
      plt.xlabel("Zaman (saniye)")
      plt.ylabel("Genlik")
      plt.show()
      

def  azaltilmis():
      M = 2 
      azaltilmis_ornek = decimate(data, M)

      
      sd.play(azaltilmis_ornek, fs)
      sd.wait()

      

      # Çizdirme
      time_downsampled = np.linspace(0, len(azaltilmis_ornek) / fs, num=len(azaltilmis_ornek))
      
      print(f"Örnekleme frekansı: {time_downsampled}")
      print(f"Toplam örnek sayısı: {len(azaltilmis_ornek)}")
      
      plt.figure(figsize=(10, 4))
      plt.plot(time_downsampled, azaltilmis_ornek)
      plt.title("Örnek Sayısı Azaltılmış Ses Dalga Formu")
      plt.xlabel("Zaman (saniye)")
      plt.ylabel("Genlik")
      plt.show()


def M_ileazaltilmis():
      M = 2 
      azaltilmis_ornek = decimate(data, M)
      new_fs = fs // M

      time_downsampled = np.linspace(0, len(azaltilmis_ornek) / new_fs, num=len(azaltilmis_ornek))
      plt.figure(figsize=(10, 4))
      plt.plot(time_downsampled, azaltilmis_ornek)
      plt.title("Örnekleme Frekansı Azaltılmış Ses Dalga Formu")
      plt.xlabel("Zaman (saniye)")
      plt.ylabel("Genlik")
      plt.show()


def   ornek_arttirma():
      L = 2 
      data_upsampled = resample(data, len(data) * L)
      print("Ornek arttirilmis ses çalıyor...")
      sd.play(data_upsampled, fs)
      sd.wait()
      time_upsampled = np.linspace(0, len(data_upsampled) / fs, num=len(data_upsampled))
      plt.figure(figsize=(10, 4))
      plt.plot(time_upsampled, data_upsampled)
      plt.title("Örnek Sayısı Artırılmış Ses Dalga Formu")
      plt.xlabel("Zaman (saniye)")
      plt.ylabel("Genlik")
      plt.show()

def L_ile_ornek():
     
      
      new_fs = fs * L
      time_upsampled = np.linspace(0, len(data_upsampled) / new_fs, num=len(data_upsampled))
      sd.play(data,new_fs)
      sd.wait()        
      plt.figure(figsize=(10, 4))
      plt.plot(time_upsampled, data_upsampled)
      plt.title("Örnekleme Frekansı Artırılmış Ses Dalga Formu")
      plt.xlabel("Zaman (saniye)")
      plt.ylabel("Genlik")
      plt.show()

while True:
    print("1) Orjinal Sesin Grafiğini çiz ve oynat \n"
          
          "2) Örnek Azaltılmış Sesin Grafiğini çiz ve oynat \n"
 
          "3) Örneği  M ile azaltılmış Grafiğini çiz ve oynat\n"
    
          "4) Örnekleme frekansını değiştirmeden L tamsayısı ile örnek arttırılmış Grafiğini çiz ve oynat \n"
          
          "5) L ile Arttırılmış Sesin Grafiğini çiz ve oynat \n"
          
          "6) Örnekleme frekansını değiştirmeden M ve L tamsayıları ile örnek oranı değişimi Grafiğini çiz ve oynat \n"
         
          "7)M ve L ile orantılı şekilde değişmiş Grafiğini çiz ve oynat \n"
        
          )
    
    
    sayi = input("Calistirmak istediginiz program? \n")

    if sayi == '1':
        orijinal_ses()
    elif sayi == '2':
        azaltilmis()

    elif sayi == '3':
        M_ileazaltilmis()

    elif sayi == '4':
        ornek_arttirma()

    elif sayi == '5':
        L = int(input("L degerini giriniz: "))
        ornek_arttirma(L)
    elif sayi =='6':
         L_ile_ornek()
         
    else:
         break

