
# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Bibliothecaire
from .forms import BibliothecaireForm

def all_librarians(request):
      librarian_data=Bibliothecaire.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  librarian_data
            else:
                  librarian_data=Bibliothecaire.objects.filter(titre = Search)

      countd = Bibliothecaire.objects.count()
      return render(request,"bibliothecaire/all_librarians.html",{'librarian_data': librarian_data,'countdt': countd})

def emprunt_book_to_librarian(request):
      form=BibliothecaireForm
      if request.method == 'POST':
            form=BibliothecaireForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/librarians')  # 4
      else:
       return render(request,"bibliothecaire/new_emprunt_to_librarian.html",{'form':form})

   

def update_librarian(request,pk):
      student_data=Bibliothecaire.objects.get(id=pk)
      form=BibliothecaireForm(instance=student_data)
      if request.method == 'POST':
            form=BibliothecaireForm(request.POST,instance=student_data)
            if form.is_valid():
                  form.save()
            return redirect('/librarians')  # 4
      else:
       return render(request,"bibliothecaire/update_librarian.html",{'form':form})   


