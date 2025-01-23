from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Osoba, Person, Product, Stanowisko, Team
from .serializers import OsobaSerializer, PersonSerializer, StanowiskoSerializer
from django.http import Http404, HttpResponse
from .cart import Cart
import datetime
from .models import Trip

# określamy dostępne metody żądania dla tego endpointu
@api_view(['GET'])
def person_list(request):
    """
    Lista wszystkich obiektów modelu Person.
    """
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def person_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Person
    :return: Response (with status and/or object/s data)
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Person.
    """
    if request.method == 'GET':
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_update(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Person
    :return: Response (with status and/or object/s data)
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    

    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])    
def person_delete(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'DELETE':
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_list(request):
    if request.method == "GET":
        osoby = Osoba.objects.filter(wlasciciel = request.user)
        serializer = OsobaSerializer(osoby, many = True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel = request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def osoba_details(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)   
    
    if request.method == "GET":
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)
    elif request.method == "DELETE":
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def osoba_search(request, substring):
    osoby = Osoba.objects.filter(imie__icontains = substring)  | Osoba.objects.filter(nazwisko__icontains = substring)
    serializer = OsobaSerializer(osoby, many = True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def stanowisko_list(request):

    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StanowiskoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)
    

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)
    
def person_list_html(request):
    # pobieramy wszystkie obiekty Person z bazy poprzez QuerySet
    persons = Person.objects.all()
    return render(request,
                  "folder_aplikacji/person/list.html",
                  {'persons': persons})

def person_detail_html(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404("Obiekt Person o podanym id nie istnieje")
    
    return render(request,
                  "folder_aplikacji/person/detail.html",
                  {'person': person})

class StanowiskoMemberView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            stanowisko = Stanowisko.objects.get(pk=pk)
        except Stanowisko.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        osoby = Osoba.objects.filter(stanowisko=stanowisko)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)
def home(response):
    return render(response, "main/home.html", {})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'folder_aplikacji/cart/detail.html', {'cart': cart})

def cart_clear(request):
    """Clear the shopping cart."""
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart_detail')


def trip_list(request):
    trips = Trip.objects.filter(available=True)  # Pobiera tylko dostępne wycieczki
    return render(request, 'trips/trip_list.html', {'trips': trips})

def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    return render(request, 'trips/trip_detail.html', {'trip': trip})

def trips_view(request):
    trips = [
        {
            'id': 1,
            'name': 'Wycieczka do Australii',
            'description': 'Ekscytująca wycieczka, podczas której będziesz mógł serfować na pięknych plażach Australii.',
            'price': 15000
        },
        # Dodaj inne wycieczki, jeśli są.
    ]
    return render(request, 'trips.html', {'trips': trips})


from django.shortcuts import redirect
from .models import Opinion
from .forms import OpinionForm

def opinions_view(request):
    if request.method == "POST":
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opinions')  # Nazwa URL-a

    form = OpinionForm()
    opinions = Opinion.objects.all().order_by('-created_at')
    return render(request, 'opinions.html', {'form': form, 'opinions': opinions})


from django.shortcuts import render, redirect
from .forms import UserImageForm
from .models import UserImage

def upload_image_view(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)  # Obsługa przesłanych plików
        if form.is_valid():
            form.save()
            return redirect('image_gallery')  # Przekierowanie do galerii zdjęć
    else:
        form = UserImageForm()

    return render(request, 'upload_image.html', {'form': form})

def image_gallery_view(request):
    images = UserImage.objects.all()  # Pobierz wszystkie zdjęcia
    return render(request, 'image_gallery.html', {'images': images})

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Utworzono konto dla {username}. Możesz się teraz zalogować.')
            return redirect('login')  # Zmień na nazwę Twojego widoku logowania
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    return render(request, 'profile.html')

