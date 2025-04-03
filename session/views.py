from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from operator import itemgetter
from .models import Utilisateur
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logouts
from django.contrib import auth,messages

# Create your views here.

 

def conx(request):
    
    if request.method == 'POST':
        email = request.POST['username']
        passwod = request.POST['psswd']
        user = authenticate(username=email,password=passwod)
        if user is not None  and User.is_active :
            auth.login(request, user)
            # if User.is_admin or User.is_superuser:
            #     return redirect('/home')
            # elif User.is_librarian:
            #     return redirect('/librarian')
            # else:
            #     return redirect('/pubisher')
        return redirect('/home')
    else:
        messages.error(request, 'invalid username or password')
        return render (request,"session.html")

        
        
                
                
            #  auth.login(request, user)
               
            #  request.session['username'] = email
            #  name = request.session['username']
                
            #     context = {
            #        'name' : name
            #    }
                # return redirect('/home',name)

        # else:
        #     messages.error(request,"Vous n'etes pas reconnus")
        #     return render(request, "session.html")
# def register(request):
#     user = Utilisateur()
#     if request.method == "POST":
#         user.name = request.POST['nom'] 
#         user.email = request.POST['mail']
#         user.cin = request.POST['cin']
#         user.password = request.POST['psswd']
#         user.save()
#         return render(request, "session.html")
#     return render (request,"registration.html")

# Publisher views

def pubisher(request):
    return render(request, 'publisher/home.html')






# Librarian views

def librarian(request):
    return render(request, 'librarian/home.html')


# Admin views

# Librarian views

def dashboard(request):
    return render(request, 'dashboard/home.html')





def register(request):
    user = Utilisateur()

    if request.method == "POST":
        user.name = request.POST.get('name')
        user.email = request.POST.get('mail')
        user.cin = request.POST.get('cin')
        user.password = request.POST.get('psswd')
        print(request.POST)

        user.save()
        return render(request, "session.html")

    return render(request, "registration.html")

def logout(request):
    if request.method == 'POST':
        logouts(request)
        del request.session['username']
        return render(request, "session.html")
    return redirect('connexion')