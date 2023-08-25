class Üyelik:
    def __init__(self,kullanıcıadi,şifre):
        self.kullanıcıadi=kullanıcıadi
        self.şifre=şifre
üyelikler=[{"kullanıcıadi":"eray61","şifre":"eray6161"}]
def kullaniciKaydı():
    print("KULLANICI KAYIT EKRANINA HOŞ GELDİNİZ")
    kullanıcıadi=input("Kullanıcı Adı: ")
    şifre=input("Şifre: ")
    yeniüyelik=Üyelik(kullanıcıadi,şifre)
    üyelikler.append(yeniüyelik)
    print("Kullanici kaydı başarılı.")
def kullaniciGirisi():
    kullanıcıadi=input("Kullanıcı Adı: ")
    şifre=input("Şifre: ")

    for kullanici in üyelikler:
        if kullanici["kullanıcıadi"] == kullanıcıadi and kullanici["şifre"] == şifre:

            print("Giriş başarılı")
            return kullanici
            
        else:
            print("Üyelik kaydınız yoktur lütfen önce kayıt yapınız. ")
                                              

class Araba:
    def __init__(self,model,renk,fiyat):
        self.model=model
        self.renk=renk
        self.fiyat=fiyat

araba1=Araba("Fiat ","Sarı,Gri",32000)
araba2=Araba("Volkswagen ","Kırmızı,Beyaz,Siyah,Gri",50000)
araba3=Araba("Isuzu ","Gri",43000)
araba4=Araba("Honda","Siyah,Beyaz,Gri",45000)
araba5=Araba("Kartal","Kırmızı,Yeşil",5000)
araba6=Araba("BMW ","Kırmızı,Mavi,Bej Gri",75000)
araba7=Araba("Mitsubishi","Gri",42000)
araba8=Araba("Audi ","Siyah,Beyaz",78000)
araba9=Araba("Aston Martin","Kırmızı",158000)
araba10=Araba("Bentley","Yeşil,Mavi",200045)
araba11=Araba("Bugatti","Kırmızı,Beyaz",465000)
araba12=Araba("Ford","Lacivert,Yeşil",35000)
araba13=Araba("Renault","Gri",30000)
araba14=Araba("Citroen","Beyaz",43000)
araba15=Araba("Peugoet","Kırmızı,Lacivert",38000)
araba16=Araba("Cupra","Bordo",250000)
araba17=Araba("Dacia","Deniz Mavisi",36500)
araba18=Araba("Ferrari","Kırmızı,Beyaz,Gri",545000)
araba19=Araba("Dodge","Sarı",478000)
araba20=Araba("Hyundai","Mat Gri",42000)
araba21=Araba("Range Rover","Parlak Siyah",145000)

arabalar=[araba1,araba2,araba3,araba4,araba5,araba6,araba7,araba8,araba9,araba10,araba11,araba12,araba13,araba14,araba15,araba16,araba17,araba18,
          araba19,araba20,araba21]

def arabalarıGoster(arabalar):
    print("{:<15} {:<20} {:<10}".format("Model", "Renk", "Fiyat"))
    print("=" * 45)
    for araba in arabalar:
        print("{:<15} {:<20} {:<10}".format(araba.model, araba.renk, araba.fiyat))

def arabaVergiliFiyatı(araba):
    kdv=0.18
    ötv=0
    if araba.fiyat<120000:
        ötv=0.45
    
    elif araba.fiyat>=120000 and araba.fiyat< 150000:
        ötv=0.50
    
    elif araba.fiyat>=150000 and araba.fiyat<175000:
        ötv=0.60
    
    elif araba.fiyat>=175000 and araba.fiyat<200000:
        ötv=0.70

    elif araba.fiyat>=200000:
        ötv=0.80
    
    arafiyat=araba.fiyat * ötv
    ötvfiyat=arafiyat + araba.fiyat
    arafiyat2=ötvfiyat * kdv
    vergiliFiyat=ötvfiyat + arafiyat2
    return vergiliFiyat
def fiyatHesaplatma():
    miktar=int(input("Lütfen vergili fiyatı hesaplatmak için miktarı giriniz: "))
    kdv=0.18
    ötv=0
    if miktar<120000:
        ötv=0.45
    
    elif miktar>=120000 and miktar< 150000:
        ötv=0.50
    
    elif miktar>=150000 and miktar<175000:
        ötv=0.60
    
    elif miktar>=175000 and miktar<200000:
        ötv=0.70

    elif miktar>=200000:
        ötv=0.80
    
    arafiyat=miktar * ötv
    ötvfiyat=arafiyat + miktar
    arafiyat2=ötvfiyat * kdv
    vergiliFiyat=ötvfiyat + arafiyat
    print(f"Vergili Fiyat: {vergiliFiyat}")
    return vergiliFiyat

def arabaEkleme(arabalar):
    model=input("Eklemek istediğiniz aracın modelini giriniz: ")
    renk=input("Eklemek istediğiniz arabanın rengini giriniz: ")
    fiyat=int(input("Eklemek istediğiniz arabanın fiyatını giriniz: "))
    araba=Araba(model,renk,fiyat)
    arabalar.append(araba)

while True:
    print("-----------ANA MENU--------")
    print("Benim Arabam'a hoşgeldiniz eğer hesabınız varsa giriş yapabilirsiniz hesabınız yoksa hesap oluşturmanız gerekmektedir.")
    print("1-Giriş")
    print("2-Kayıt Ol")
    secim=int(input("Yapmak istediğiniz işlemi seçiniz:"))
    if secim==1:
        if kullaniciGirisi():
            while True:

                print("-----------MENU---------")
                print("1-Vergisiz Fiyat")
                print("2-Vergili Fiyat")
                print("3-İstediğiniz fiyatı girerek buradan vergili fiyatı hesaplatabilirsiniz.")
                print("4-Araba Ekleme")
    
                secim=int(input("Yapmak istediğiniz işlemi seçiniz:"))
                if secim==1:
                    arabalarıGoster(arabalar)
                elif secim==2:
                    print("{:<15} {:<20} {:<10}".format("Model", "Renk", "Vergili Fiyat"))
                    print("=" * 45)
                    for araba in arabalar:
                        vergiliFiyat=arabaVergiliFiyatı(araba)
                        print("{:<15} {:<20} {:<10}".format(araba.model, araba.renk, vergiliFiyat))
                elif secim==3:
                    fiyatHesaplatma()
                elif secim==4:
                    arabaEkleme(arabalar)
                    print("Araba ekleme başarılı. 4")

                else:
                    print("Geçersiz seçim lütfen 1-2-3 menülerinden birisini seçiniz. ")

    if secim==2:
        kullaniciKaydı()

                



   



