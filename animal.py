class Animal:  # Loome baasklassi Animal

    def __init__(self, pet_name):  # Konstruktor, käivitub objekti loomisel
        self.name = pet_name  # Salvestab looma nime
        self.ears = 2  # Loomal on 2 kõrva
        self.legs = 4  # Loomal on 4 jalga

    def sees(self, other):  # Meetod, kui loom näeb teist objekti
        print(f"{self.name} sees {other.name}.")  # Kuvab, keda loom näeb


class Cat(Animal):

    def __init__(self, cat_name):
        super().__init__(cat_name)
        self.hunger = 9  # Kass on juba üsna näljane

    def meow(self):  # Kassi näugumise meetod
        print(f"{self.name}: Meow!")  # Kass näugub

    def sleep(self):  # Kassi magamise meetod
        print(f"{self.name} is sleeping...")  # Kass magab

        self.hunger = self.hunger + 1  # Suurendab nälga ühe võrra

        if self.hunger >= 10:  # Kui nälg jõuab 10-ni
            print(f"{self.name} wakes up hungry!")  # Kass ärkab näljasena
            self.meow()  # Kass näugub

    def hiss(self):  # Kassi sisistamise meetod
        print(f"{self.name}: Hissss!")  # Kass sisiseb

    def cat_sees(self, other):  # Meetod, mida kass teeb teist objekti nähes
        super().sees(other)  # Kasutab Animal klassi sees() meetodit

        if isinstance(other, Dog):  # Kontrollib, kas kass näeb koera
            self.hiss()  # Kui näeb koera, siis sisiseb


class Dog(Animal):  # Dog pärib Animal klassist

    def __init__(self, dog_name):  # Dog klassi konstruktor
        super().__init__(dog_name)  # Käivitab Animal klassi konstruktori
        self.is_running = False  # Alguses koer ei jookse autole järgi

    def bark(self):  # Koera haukumise meetod
        print(f"{self.name}: Woof!")  # Koer haugub

    def wag_the_tail(self):  # Saba liputamise meetod
        print(f"{self.name} is wagging its tail.")  # Koer liputab saba

    def run_after(self, other):  # Meetod autole järgi jooksmiseks
        self.is_running = True  # Märgib, et koer jookseb
        print(f"{self.name} runs after {other.name}!")  # Kuvab tegevuse

    def dog_sees(self, other):  # Meetod, mida koer teeb teist objekti nähes
        super().sees(other)  # Kasutab Animal klassi sees() meetodit

        if isinstance(other, Cat):  # Kui koer näeb kassi
            self.bark()  # Koer haugub

        elif isinstance(other, Car):  # Kui koer näeb autot
            self.bark()  # Koer haugub
            self.run_after(other)  # Koer hakkab autole järgi jooksma

        else:  # Kui näeb midagi muud
            self.wag_the_tail()  # Koer liputab saba


class Car:  # Loome eraldi Car klassi

    def __init__(self, car_name, speed):  # Auto konstruktor
        self.name = car_name  # Salvestab auto nime
        self.speed = speed  # Salvestab auto algkiiruse

    def accelerate(self):  # Auto kiirendamise meetod
        self.speed = self.speed + 10  # Suurendab kiirust 10 võrra
        print(f"{self.name} accelerates to {self.speed} km/h!")  # Kuvab uue kiiruse

    def car_sees(self, other):  # Meetod, mida auto teeb teist objekti nähes
        print(f"{self.name} sees {other.name}.")  # Auto näeb objekti

        if isinstance(other, Dog) and other.is_running:  # Kui koer jookseb autole järgi
            self.accelerate()  # Auto kiirendab