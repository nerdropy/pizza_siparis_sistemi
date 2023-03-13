import csv
import datetime

menu = """"
* Lütfen Bir Pizza Tabani Seçiniz:
1: Klasik
2: Margarita
3: TürkPizza
4: Sade Pizza
* ve seçeceğiniz sos:
11: Zeytin
12: Mantarlar
13: Keçi Peyniri
14: Et
15: Soğan
16: Misir
* Teşekkür ederiz!"""

with open('menu.txt', 'w', encoding="utf-8") as f:
    f.write(menu)

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

class Klasik(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)

class Margarita(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
    
class TurkPizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)
    
class SadePizza(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)

class Toppings:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Zeytin(Toppings):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost
    
class Mantarlar(Toppings):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost

class Keci_Peyniri(Toppings):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost

class Et(Toppings):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost

class Sogan(Toppings):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost

class Misir(Toppings):
    def __init__(self, description, cost):
        super().__init__( description, cost)
        self.description = description
        self.cost = cost

class Decorator:
    def __init__(self, pizza_fiyat, topping_secim):
        self.pizza = pizza_fiyat
        self.topping_desc = ''
        self.topping_top = 0
        for topping_fiyat in topping_secim:
            self.topping_top += topping_fiyat.get_cost()
            self.topping_desc += ' ve ' + topping_fiyat.get_description()

    def get_cost(self):
        return self.pizza.get_cost() + self.topping_top
    
    def get_description(self):
        return self.pizza.get_description() + self.topping_desc

class Musteri:
    def __init__(self, isim, tc, kredi, sifre):
        self.isim = isim
        self.tc = tc
        self.kredi = kredi
        self.sifre = sifre

def siparis():
    with open("Menu.txt","r",encoding="utf-8") as f:
        menu=f.read()
        print(menu)
    
    secim = int(input("Lutfen pizza seciniz: "))
    match secim:
        case 1:
            pizza = Klasik("Klasik Pizza", 60)
        case 2:
            pizza = Margarita("Margarita", 40)
        case 3:
            pizza = TurkPizza("Türk Pizza", 85)
        case 4:
            pizza = SadePizza("Sade Pizza", 45)
        case _:
            print("Hatali secim yaptiniz.")
            return None
        
    ek_malzemeler = []
    while True:
        secim = input("Lutfen ek malzeme seciniz. Secim bitince x'e basiniz. ")

        match secim:
            case '11':
                malzeme = Zeytin("Zeytin", 2)
                ek_malzemeler.append(malzeme)
            case '12':
                malzeme = Mantarlar("Mantarlar", 4)
                ek_malzemeler.append(malzeme)                
            case '13':
                malzeme = Keci_Peyniri("Keci Peyniri", 9)
                ek_malzemeler.append(malzeme)
            case '14':
                malzeme = Et("Et", 15)
                ek_malzemeler.append(malzeme)
            case '15':
                malzeme = Sogan("Sogan", 1)
                ek_malzemeler.append(malzeme)
            case '16':
                malzeme = Misir("Misir", 3)
                ek_malzemeler.append(malzeme)
            case 'x':
                break
            case _:
                print("Hatali secim yaptiniz.")  

    pizza_ve_toppings = Decorator(pizza, ek_malzemeler)

    isim = input("Isminiz: ")
    tc = input("TC: ")
    kredi = input("Kredi karti no: ")
    sifre = input("Kredi karti sifre: ")

    print("Siparisiniz hazir. Seciminiz: ", pizza_ve_toppings.get_description())
    print(" Ucret: ", pizza_ve_toppings.get_cost(), " TL" )

    tarih = datetime.datetime.now()
    with open("Orders_Database.csv", "a", newline="") as f:
        cikti = csv.writer(f)
        cikti.writerow(['*********************\n' + 'Siparisi veren kisinin ismi: ' + isim])
        cikti.writerow(['TC Kimlik No' + tc])
        cikti.writerow(['Kredi karti no: ' + kredi])
        cikti.writerow(['Siparis tarihi: ' + tarih.strftime("%Y-%m-%d %H:%M:%S")])
        cikti.writerow(['Siparis ozeti: ' + str(pizza_ve_toppings.get_description())])
        cikti.writerow(['Siparis tutari: ' + str(pizza_ve_toppings.get_cost())])
        cikti.writerow(['Kredi karti sifre: ' + sifre + '\n*********************'])


siparis()
