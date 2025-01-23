# plik ankiety/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name="home"), #strona domyslna
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('persons/update/<int:pk>/', views.person_update),
    path('persons/delete/<int:pk>/', views.person_delete),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_details),
    path('osoby/search/<str:substring>/', views.osoba_search),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>', views.stanowisko_detail),
    path('welcome/', views.welcome_view),
    path('persons_html/', views.person_list_html),
    path('persons_html/<int:id>', views.person_detail_html, name="persons_html_detail"),
    path("persons_html/<int:id>", views.person_detail_html),
    path('stanowisko/<int:pk>/members', views.StanowiskoMemberView.as_view()),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('trips/', views.trips_view, name='trips_list'),
    path('opinions/', views.opinions_view, name='opinions'),
    path('upload_image/', views.upload_image_view, name='upload_image'),
    path('image_gallery/', views.image_gallery_view, name='image_gallery'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]