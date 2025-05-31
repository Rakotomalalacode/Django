import random
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializers import FilmSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Application.models import Film
from .forms import LoginForm

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')  # Remplacez par votre URL de redirection
#             else:
#                 messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
#     else:
#         form = LoginForm()
    
#     return render(request, '/film/Login.html', {'form': form})

@api_view(['GET'])
def api_film_list(request):
    films=Film.objects.all()
    serializer = FilmSerializer(films, many=True)
    return Response(serializer.data)    

def Hello (request) :
    films = Film.objects.all()
    films = list(films)
    random.shuffle(films)
    
    films_aleatoire = random.choices(films, k=4)
    
    return render(request , 'film/Hello.html', {"films_aleatoire": films_aleatoire})
def toggle_theme (request):
    current_theme = request.session.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    request.session['theme'] = new_theme
    return redirect(request.META.get('HTTP_REFERER', '/'))
def Login (request):
    return render(request , 'film/Login.html')
def Register(request):
    return render(request , 'film/Register.html')
def Dashboard(request):
    return render(request , 'film/Dashboard.html')
def yourName(request):
    return render(request , 'film/yourName.html')
def Profile(request):
    return render(request , 'film/Profile.html')
def mylist (request):
    return render(request , 'film/mylist.html')
def newFilm (request):
    return render(request , 'film/newFilm.html')