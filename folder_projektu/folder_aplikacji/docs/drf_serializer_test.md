from folder_aplikacji.models import Osoba, Stanowisko
from folder_aplikacji.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# tworzymy nowe objekty
stanowisko = Stanowisko.objects.create(nazwa = "Kierownik", opis = "zarzadza tymi co zarzadzaja")
osoba = Osoba.objects.create(imie = "Jan", nazwisko = "Malinowski", plec = 2, stanowisko = stanowisko)

# inicjalizacja serializer dla osoba
osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)

# ['id':6, 'imie': 'Jan', 'nazwisko': 'Malinowski', 'plec':'męzczyzna', 'stanowisko': stanowisko.id, 'osoba.data_dodania': '2024-12-2]


osoba_json = JSONRenderer().render(osoba_serializer.data)
# ['id':6, 'imie': 'Jan', 'nazwisko': 'Malinowski', 'plec':'męzczyzna', 'stanowisko': 4, 'data_dodania': '2024-12-2]


import io
# strumien json
stream = io.BytesIO(osoba_json)

# pasowanie JSON do slownika
data = JSONParser().parse(stream)

# tworzymy obiekt deserializera dla danych JSON
deserializer = OsobaSerializer(data = data)

# walidacja danych
print(deserializer.is_valid())
print(deserializer.errors)


# oczekiwany wynik -> True

# błędne dane
invalid_data = {'imie':'Adam', 'nazwisko': 'Nowak','plec': 'nieznane','stanowisko':'stanowisko.id'}
invalid_serializer = OsobaSerializer(data = invalid_data)
print(invalid_serializer.is_valid())
print(invalid_serializer.errors)

# false
# ['plec':["nieznany" is not a valid choice']]


# zapis do bazy danych
if deserializer.is_valid():
    deserializer.save()

# inicjowanie serializera dla stanowiska
stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)

# {'id':3, 'nazwa': "Kierownik", 'opis' : "zarzadza tymi co zarzadzaja"}


# serializacja do json

stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print(stanowisko_json)
# {'id':3, 'nazwa': "Kierownik", 'opis' : "zarzadza tymi co zarzadzaja"}


# deserializacja z JSON
stream = io.BytesIO(stanowisko_json)
data = JSONParser().parse(stream)

deserializer = StanowiskoSerializer(data = data)
print(deserializer.is_valid())

if deserializer.is_valid():
    deserializer.save()

