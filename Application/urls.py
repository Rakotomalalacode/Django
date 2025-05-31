from django.urls import path
from .views import Hello, toggle_theme, mylist, newFilm, Login, Register, Profile, Dashboard, api_film_list

urlpatterns = [
    path('', Hello, name='Hello'),
    path('/toggle_theme', toggle_theme , name='toggle_theme'),
    path('/login', Login , name='login'),
    path('/register', Register , name='register'),
    path('/dashboard', Dashboard , name='dashboard'),
    path('/profile', Profile , name='profile'),
    path('/myList', mylist , name='mylist'),
    path('/newFilm' , newFilm , name='newFilm'),
    path('api/films', api_film_list, name='api_film_list')
]
