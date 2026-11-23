from animal import Animal, Cat, Dog, Car


my_cat = Cat("Fluffy")  # Loob kassi nimega Fluffy

my_dog = Dog("Rex")  # Loob koera nimega Rex

neighbours_dog = Dog("Chilly")  # Loob naabrikoera nimega Chilly

passing_car = Car("BMW", 50)  # Loob auto BMW algkiirusega 50 km/h


# 1. Kass ärkab näljasena
my_cat.sleep()

# 2. Kass näeb koera ja sisiseb
my_cat.cat_sees(my_dog)

# 3. Koer näeb kassi ja haugub
my_dog.dog_sees(my_cat)

# 4. Koer näeb möödasõitvat autot, haugub ja jookseb sellele järgi
my_dog.dog_sees(passing_car)

# 5. Auto näeb järgijooksvat koera ja kiirendab
passing_car.car_sees(my_dog)

# 6. Kõige lõpus näeb Rex naabrikoera Chillyt
my_dog.dog_sees(neighbours_dog)