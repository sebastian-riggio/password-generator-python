import random
from django.shortcuts import render
#from django.http import HttpResponse



def home (request):
      return  render(request, 'home.html')
  
def about(request):
  return  render(request, 'about.html')


def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')  
    generated_password = ''
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=*-+=<>?/,.[]}{;:`~|'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    

    for x in range(length): 
        generated_password += random.choice(characters)
    
    return render(request, 'password.html', {'password': generated_password})

