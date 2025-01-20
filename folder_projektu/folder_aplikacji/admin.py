from django.contrib import admin

# Register your models here.
from .models import Team, Person, Osoba, Stanowisko

admin.site.register(Team)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'shirt_size', 'team']
    list_filter = ['team']
admin.site.register(Person, PersonAdmin)
admin.site.register(Stanowisko)

class OsobaAdmin(admin.ModelAdmin):
    class StanowiskoAdmin(admin.ModelAdmin):
        list_filter = ["nazwa"]
        list_display = ["nazwa", "opis"]

    @admin.display(description="Stanowisko (ID)")
    def stanowisko_with_id(self,obj):
        if obj.stanowisko:
            return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'
        return 'Brak stanowiska'
    list_display = ["imie", "nazwisko", "plec", "stanowisko_with_id", "data_dodania"]
    list_filter = ["stanowisko", "data_dodania"]
admin.site.register(Osoba, OsobaAdmin)