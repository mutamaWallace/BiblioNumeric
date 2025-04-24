from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from operator import itemgetter
from .models import Utilisateur
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logouts
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
# Create your views here.



def conx(request):
    
    if request.method == 'POST':
        email = request.POST['username']
        passwod = request.POST['psswd']
        user = authenticate(username=email,password=passwod)
        if user is not None :
            auth.login(request, user)
            # if User.is_admin or User.is_superuser:
            #     return redirect('/home')
            # elif User.is_librarian:
            #     return redirect('/librarian')
            # else:
            #     return redirect('/pubisher')
        return redirect('/home')
    else:
        # messages.error(request, 'invalid username or password')
        return render (request,"session.html")

        
# Publisher views

def pubisher(request):
    return render(request, 'publisher/home.html')

# Librarian views


def librarian(request):
    return render(request, 'librarian/home.html')


# Admin views
# Librarian views



from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def dashboard(request):
    if not request.user.has_perm('product.dashboard'):
        return HttpResponseForbidden("Vous n'avez pas la permission d’accéder au tableau de bord.")




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