from ast import NameConstant
from django.shortcuts import render,redirect
from auteurs.models import Auteurs
from livre.models import Livre
# from rest_framework.response import Response
from Fournisseur.models import Fourn
from django.db.models import Q
from auteurs.forms import AuteursForm
# Create your views here.



def allauthors(request):
    aut_data = Auteurs.objects.all()
    
    # Vérifie si une recherche a été effectuée
    if 'Search' in request.GET:
        search = request.GET['Search'].strip()  # Supprime les espaces inutiles
        
        if search:
            # Filtrer les auteurs par nom, prénom ou postnom
            aut_data = Auteurs.objects.filter(
                Q(nom__icontains=search) | 
                Q(prenom__icontains=search) | 
                Q(postnom__icontains=search)
            )
    
    countdt = aut_data.count()  # Compte le nombre d'auteurs après filtrage
    return render(request, "Auteur/aut.html", {'aut_data': aut_data, 'countdt': countdt})

# def all_authors(request):
#       aut_data=Auteurs.objects.all()
#       if 'Search' in request.GET:
            
#             Search=request.GET['Search']
#             if Search=="":
#                   aut_data
#             else:
#                   aut_data=Auteurs.objects.filter(nom =Search, prenom = Search, postnom = Search)
#       countdt = Auteurs.objects.count()
#       return render(request,"Auteur/aut.html",{'aut_data':aut_data,'countdt': countdt})

def create_author(request):
      form=AuteursForm
      if request.method == 'POST':
            form=AuteursForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/all_authors')  # la page des auteurs pour 
      else:
       return render(request,"Auteur/new_author.html",{'form':form})

def update_author(request,Id):
      aut_data=Auteurs.objects.get(Id=Id)
      form=AuteursForm(instance=aut_data)
      if request.method == 'POST':
            form=AuteursForm(request.POST,instance=aut_data)
            if form.is_valid():
                  form.save()
            return redirect('/all_authors')  # 4
      else:
       return render(request,"Auteur/update_author.html",{'form':form})

def delete_author(request,Id):
      aut_data=Auteurs.objects.get(Id=Id)
      aut_data.delete()
      return redirect('/all_authors')
