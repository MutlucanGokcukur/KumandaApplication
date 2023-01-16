# -*- coding: cp1254 -*-
import random
import time

class Kumanda():
    def __init__(self,tv_durumu="Kapalı",tv_ses=0,kanal_listesi=["TRT Spor","TRT 1","TRT Belgesel"],kanal="TRT"):
        self.tv_durumu=tv_durumu
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if self.tv_durumu=="Açık":
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor...")
            time.sleep(1)
            self.tv_durumu="Açık" 

    def tv_kapa(self):
        if self.tv_durumu=="Kapalı":
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon kapanıyor...")
            time.sleep(1)
            self.tv_durumu="Kapalı"

    def ses_ayarla(self):
        while True:
            print("Ses arttırmak için '+' tuşuna basınız\nSes azaltmak için'-' tuşuna basınız\nÇıkış için '0' basınız")
            ses=input("Seçiminiz: ")
            if ses=="+":
                if self.tv_ses<100:
                    self.tv_ses+=5
                    print("Televizyon ses seviyesi: {}".format(self.tv_ses))
                elif self.tv_ses>=100:
                    self.tv_ses=100
                    print("Sağlığınız için maksimum ses seviyesi '100' olarak ayarlandı...")
            elif ses=="-":
                if self.tv_ses<0:
                    print("Ses 0'ın altına düşemez...")
                else:
                    self.tv_ses-=5
                    print("Televizyon ses seviyesi: {}".format(self.tv_ses))
            elif ses=="0":
                break
            else:
                print("Geçersiz işlem girildi...")
    
    def kanal_ekle(self,kanal_ismi):
        print("Girilen kanal listeye ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal başarıyla listeye eklendi...")
    
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Açık olan kanal: {}".format(self.kanal))
    
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "TV durum: {}\nSes seviyesi: {}\nAçık olan kanal: {}".format(self.tv_durumu,self.tv_ses,self.kanal)



print("""
Televizyon Uygulaması
1-Televizyon Aç
2-Televizyon Kapat
3-Ses Ayarları
4-Kanal Ekle
5-Kanal Sayısı Öğrenme
6-Rastgele Kanal Değiştirme
7-Televizyon Bilgileri
0-Çıkış
""")

kumanda=Kumanda()
while True:
    secim=int(input("İşlem numarasını giriniz: "))

    if secim==1:
        kumanda.tv_ac()
    elif secim==2:
        kumanda.tv_kapa()
    elif secim==3:
        kumanda.ses_ayarla()
    elif secim==4:
        kanal=input("Birden fazla kanal gireceksiniz ',(virgül)' ile ayırınız...\nEklemek istediğiniz kanal ya da kanalları giriniz: ")
        kanalliste=kanal.split(",")
        for x in kanalliste:
            kumanda.kanal_ekle(x)
    elif secim==5:
        print("Televizyonda kayıtlı toplam kanal sayısı: {}".format(len(kumanda)))
    elif secim==6:
        print("Rastgele kanal seçiliyor...")
        time.sleep(1)
        kumanda.rastgele_kanal()
    elif secim==7:
        print(kumanda)
    elif secim==0:
        print("Program sonlandırılıyor...")
        time.sleep(1)
        break
    else:
        print("Geçersiz işlem numarası girildi...")
