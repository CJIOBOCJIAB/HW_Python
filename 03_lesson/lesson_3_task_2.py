from smartphone import Smartphone

catalog=[
    Smartphone("Zukko", "01-10", "+7 123 321 45 54"),
    Smartphone("Rabson", "02-234", "+7 321 246 76 90"),
    Smartphone("KioToo","I-33","+7 132 999 45 45"),
    Smartphone("KioToo","I-34","+7 132 999 45 46"),
    Smartphone("KioToo","I-35","+7 132 999 45 47")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.ab_number}")
