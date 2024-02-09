from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def room(request):
    if request.method == 'POST':
      room_name = request.POST.get('room_name', '')
      username = request.POST.get('username', '')
      return render(request, 'room.html', {'room_name': room_name, 'username': username})
    else:
      return HttpResponse("Invalid request method. Expected POST.")
