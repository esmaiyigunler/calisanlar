class GenelCalisan:
    def __init__(self,maas,departman):
        self.maas=maas
        self.departman=departman
    def bilgi(self):
        print(f"Maaş: {self.maas}, Departman: {self.departman}")
class Mudur(GenelCalisan):
    def __init__(self,maas,departman,calisanSayisi):
        super().__init__(maas,departman)
        self.calisanSayisi=calisanSayisi
    def bilgi(self):
        super().bilgi()
        print(f"calisan sayısı: {self.calisanSayisi}")
class Yonetici(Mudur):
    def __init__(self,maas,departman,calisanSayisi,butce):
        super().__init__(maas,departman,calisanSayisi)
        self.butce=butce
    def bilgi(self):
        super().bilgi()
        print(f"butce: {self.butce}")
genel=GenelCalisan(4000,"IT")
mudur=Mudur(7000,"Satış",2)
yonetici=Yonetici(12222,"Finans",20,45000)
genel.bilgi()
print()
mudur.bilgi()
print()
yonetici.bilgi()
print()
    
