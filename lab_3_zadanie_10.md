 Zadanie 1 
 ```
 from folder_aplikacji.models import Osoba
 osoby = Osoba.objects.all()
 print(osoby)
 ```

 Zadanie 2
 ```python
osoba = Osoba.objects.get(id=3)
print(osoba)
Daniel Magiczny

 ```

 Zadanie 3 
 ```python
osoba = Osoba.objects.get(id=3)
print(osoba)
Daniel Magiczny
```

Zadanie 4
```python
Osoba.objects.values('stanowisko').distinct()
```
Zadanie 5 
```python
from folder_aplikacji.models import Stanowisko
Stanowisko.objects.values_list('nazwa', flat = True).order_by("-nazwa")
```
Zadanie 6
```python
from folder_aplikacji.models import Stanowisko
Osoba.objects.create(imie='Jan', nazwisko='Kowalski', plec='M', Stanowisko.objects.get(id=1))
```
