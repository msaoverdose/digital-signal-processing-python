import librosa
from scipy.signal import decimate, resample, resample_poly
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

#Digital Signal Processing - Nur Hüseyin Kaplan
#Ödevi yapan: Mehmet Semih ARSLAN 210302027
#Projede Ses işleme ve analiz için, librosa
#Örnekleme azaltma ve yeniden örnekleme için scipy.signal
#Veri görselleştirme için, matplotlib
#Ses dosyalarını oynatmak için, sounddevice kütüphanelerinden yararlanılmıştır.
#Tekrarlanan kodların açıklaması yapılmamıştır.

########################################################################################

dosya_yolu = '/home/msa/Desktop/sayısal.i.t/digital-signal-processing-python/sound.mp3' #Ses dosya yolu, Linux kullandığım için Wİndows işletim sistemlerinde bu dosya dizini sıkıntı çıkartabiliyor.
veri, fs = librosa.load(dosya_yolu, sr=None, mono=True) #Ses verimizi sayısal dizi olarak döndürür. sr=None, mono=True; orjinal ses dosyasındaki veriyi alır ve mono sesi tek kanlları işler.

def orijinal_ses():
    #Sesi oynatmak için kullanılan kodlar.
    sd.play(veri, fs) 
    sd.wait()
    zaman = np.linspace(0, len(veri) / fs, num=len(veri)) #Sesin başladığı andan (yani 0 anından) bitiş kısımına kadar kısmı bir dizi olarak oluşturur. Daha sonrasında sesin her örneği için bir zaman değeri atanır.

    #Grafik çizdirmek için kullanılan kodlar.
    plt.figure(figsize=(10, 4))
    plt.plot(zaman, veri) #Sesin her anı için grafikte sesin değerini grafiğe döker

    plt.title(f"Orijinal Ses Dalga Formu (Örnek Sayısı: {len(veri)}, F(s) = {fs} Hz)" ) 
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

def azaltma():
    M = 2  # Örnekleme azaltma faktörü
    azaltilmis_veri = decimate(veri, M)  # Veriyi örnekleme oranı ile azalt
    
    # Yeni örnekleme frekansını hesapla
    
    # Azaltılmış sesin çalınması
    print("Azaltılmış ses çalıyor...")
    sd.play(azaltilmis_veri, fs)
    sd.wait()

    # Zaman dizisini oluştur
    zaman_azaltilmis = np.linspace(0, len(azaltilmis_veri) / (fs//M), num=len(azaltilmis_veri))
    
    # Grafik çizimi
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_azaltilmis, azaltilmis_veri)
    plt.title(f"Örnek Sayısı Azaltılmış Ses Dalga Formu (Örnek Sayısı: {len(azaltilmis_veri)}, F(s) = {fs//M} Hz)")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()




def M_ile_azaltilmis():
    M = 2
    azaltilmis_veri = decimate(veri, M) 
    zaman_azaltilmis = np.linspace(0, len(azaltilmis_veri) / (fs//M), num=len(azaltilmis_veri))
    sd.play(azaltilmis_veri, fs)
    sd.wait()
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_azaltilmis, azaltilmis_veri)
    plt.title(f"Örnekleme Frekansı Azaltılmış (Örnek Sayısı: {len(azaltilmis_veri)}, F(s) = {(fs//M)} Hz)")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

def ornek_arttirma_L():
    L = 2
    arttirilmis_veri = resample(veri, len(veri) * L) #L ile çarpılarak örnek arttırılır
    sd.play(arttirilmis_veri, fs)
    sd.wait()
    zaman_arttırılmış = np.linspace(0, len(arttirilmis_veri) / fs, num=len(arttirilmis_veri))
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_arttırılmış, arttirilmis_veri)
    plt.title(f"Örnek Sayısı Artırılmış (Örnek Sayısı: {len(arttirilmis_veri)}, F(s) = {(fs*L)} Hz)")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

def fs_ile_arttirma():
    L = 2
    arttirilmis_veri = resample_poly(veri, L, 1)
    sd.play(arttirilmis_veri, fs) #Örnek sayısı arttırılır ve ses kalınlaşır
    sd.wait()
    zaman_arttırılmış = np.linspace(0, len(arttirilmis_veri) / fs, num=len(arttirilmis_veri))
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_arttırılmış, arttirilmis_veri)
    plt.title(f"Örnekleme Frekansı Artırılmış (Örnek Sayısı: {len(arttirilmis_veri)}, F(s) = {(fs*L)} Hz)")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

def ornek_orani_degisimi_M_L():
    M = 2
    L = 3
    oranli_veri = resample_poly(veri, L, M) #Polinom interpolasyonu kullanarak sinyali yeniden örnekler
    sd.play(oranli_veri, fs)
    sd.wait()
    zaman_oranli = np.linspace(0, len(oranli_veri) / fs, num=len(oranli_veri))
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_oranli, oranli_veri)
    plt.title(f"Örnek Oranı Değişmiş (Örnek Sayısı: {len(oranli_veri)}, F(s) = {(fs//M)*L} Hz)")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

def fs_orani_degisimi_M_L():
    M = 2
    L = 3
    oranli_veri = resample_poly(veri, L, M)  
    yeni_fs = fs * L // M #farklı bir fs değerine atarak yaptığımız oran işlemi
    sd.play(oranli_veri, fs)
    sd.wait()
    zaman_oranli = np.linspace(0, len(oranli_veri) / fs, num=len(oranli_veri))
    plt.figure(figsize=(10, 4))
    plt.plot(zaman_oranli, oranli_veri)
    plt.title(f"Örnekleme Frekansı Orantılı Değişmiş (Örnek Sayısı: {len(oranli_veri)}, F(s) = {yeni_fs} Hz)")
    plt.xlabel("Zaman (saniye)")
    plt.ylabel("Genlik")
    plt.show()

while True:
    #Kullanım kolaylığı için terminal kodu
    print("1) Orjinal Ses Grafiği ve Oynat\n"
          "2) Örnek Azaltılmış Ses Grafiği ve Oynat\n"
          "3) Örneği M ile azaltılmış Grafiği ve Oynat\n"
          "4) Örnekleme frekansını değiştirmeden L ile örnek artırılmış Grafiği ve Oynat\n"
          "5) Örnekleme frekansı L ile artırılmış Grafiği ve Oynat\n"
          "6) Örnek Oranı M ve L ile Değişmiş Ses Grafiği ve Oynat\n"
          "7) Örnekleme frekansı M ve L ile Orantılı Değişmiş Ses Grafiği ve Oynat\n"
          "Diger) Çıkış \n")
    
    sayi = input("Çalıştırmak istediğiniz program: ")

    #TErminalde kodu yönlendirmemiz için kullanılan kod

    if sayi == '1':
        orijinal_ses()
    elif sayi == '2':
        azaltma()
    elif sayi == '3':
        M_ile_azaltilmis()
    elif sayi == '4':
        ornek_arttirma_L()
    elif sayi == '5':
        fs_ile_arttirma()
    elif sayi == '6':
        ornek_orani_degisimi_M_L()
    elif sayi == '7':
        fs_orani_degisimi_M_L()
    else:
        break