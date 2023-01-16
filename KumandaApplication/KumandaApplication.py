# -*- coding: cp1254 -*-
import random
import time

class Kumanda():
    def __init__(self,tv_durumu="Kapal�",tv_ses=0,kanal_listesi=["TRT Spor","TRT 1","TRT Belgesel"],kanal="TRT"):
        self.tv_durumu=tv_durumu
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if self.tv_durumu=="A��k":
            print("Televizyon zaten a��k")
        else:
            print("Televizyon a��l�yor...")
            time.sleep(1)
            self.tv_durumu="A��k" 

    def tv_kapa(self):
        if self.tv_durumu=="Kapal�":
            print("Televizyon zaten kapal�")
        else:
            print("Televizyon kapan�yor...")
            time.sleep(1)
            self.tv_durumu="Kapal�"

    def ses_ayarla(self):
        while True:
            print("Ses artt�rmak i�in '+' tu�una bas�n�z\nSes azaltmak i�in'-' tu�una bas�n�z\n��k�� i�in '0' bas�n�z")
            ses=input("Se�iminiz: ")
            if ses=="+":
                if self.tv_ses<100:
                    self.tv_ses+=5
                    print("Televizyon ses seviyesi: {}".format(self.tv_ses))
                elif self.tv_ses>=100:
                    self.tv_ses=100
                    print("Sa�l���n�z i�in maksimum ses seviyesi '100' olarak ayarland�...")
            elif ses=="-":
                if self.tv_ses<0:
                    print("Ses 0'�n alt�na d��emez...")
                else:
                    self.tv_ses-=5
                    print("Televizyon ses seviyesi: {}".format(self.tv_ses))
            elif ses=="0":
                break
            else:
                print("Ge�ersiz i�lem girildi...")
    
    def kanal_ekle(self,kanal_ismi):
        print("Girilen kanal listeye ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal ba�ar�yla listeye eklendi...")
    
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("A��k olan kanal: {}".format(self.kanal))
    
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "TV durum: {}\nSes seviyesi: {}\nA��k olan kanal: {}".format(self.tv_durumu,self.tv_ses,self.kanal)



print("""
Televizyon Uygulamas�
1-Televizyon A�
2-Televizyon Kapat
3-Ses Ayarlar�
4-Kanal Ekle
5-Kanal Say�s� ��renme
6-Rastgele Kanal De�i�tirme
7-Televizyon Bilgileri
0-��k��
""")

kumanda=Kumanda()
while True:
    secim=int(input("��lem numaras�n� giriniz: "))

    if secim==1:
        kumanda.tv_ac()
    elif secim==2:
        kumanda.tv_kapa()
    elif secim==3:
        kumanda.ses_ayarla()
    elif secim==4:
        kanal=input("Birden fazla kanal gireceksiniz ',(virg�l)' ile ay�r�n�z...\nEklemek istedi�iniz kanal ya da kanallar� giriniz: ")
        kanalliste=kanal.split(",")
        for x in kanalliste:
            kumanda.kanal_ekle(x)
    elif secim==5:
        print("Televizyonda kay�tl� toplam kanal say�s�: {}".format(len(kumanda)))
    elif secim==6:
        print("Rastgele kanal se�iliyor...")
        time.sleep(1)
        kumanda.rastgele_kanal()
    elif secim==7:
        print(kumanda)
    elif secim==0:
        print("Program sonland�r�l�yor...")
        time.sleep(1)
        break
    else:
        print("Ge�ersiz i�lem numaras� girildi...")
