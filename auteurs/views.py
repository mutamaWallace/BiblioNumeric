# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Auteurs
from .forms import AuteursForm
# Create your views here.
def all_authors(request):
      aut_data=Auteurs.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  aut_data
            else:
                  aut_data=Auteurs.objects.filter(nom =Search, prenom = Search, postnom = Search)

      countdt = Auteurs.objects.count()
      return render(request,"Auteurs/auteur.html",{'aut_data':aut_data,'countdt': countdt})

def new_author(request):
      form=AuteursForm
      if request.method == 'POST':
            form=AuteursForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/all_authors')  # 4
      else:
       return render(request,"Auteurs/add_author.html",{'form':form})

def update_Author(request,Id):
      aut_data=Auteurs.objects.get(Id=Id)
      form=AuteursForm(instance=aut_data)
      if request.method == 'POST':
            form=AuteursForm(request.POST,instance=aut_data)
            if form.is_valid():
                  form.save()
            return redirect('/all_authors')  # 4
      else:
       return render(request,"Auteurs/update_Author.html",{'form':form})

def delete_Author(request,Id):
      aut_data=Auteurs.objects.get(Id=Id)
      aut_data.delete()
      return redirect('/all_authors')