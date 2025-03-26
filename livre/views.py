
# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Livre
from .forms import LivreForm
# Create your views here.
# def all_book(request):
#       empla_data=Livre.objects.all()
#       if 'Search' in request.GET:
            
#             Search=request.GET['Search']
#             if Search=="":
#                   empla_data
#             else:
#                   empla_data=Livre.objects.filter(Nom =Search)

#       countdt = Livre.objects.count()
#       return render(request,"emplacement/all_emplacement.html",{'etgr_data':empla_data,'countdt': countdt})

def all_book(request):
      book_data=Livre.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  book_data
            else:
                  book_data=Livre.objects.filter(titre = Search)

      countd = Livre.objects.count()
      return render(request,"livre/all_book.html",{'book_data':book_data,'countdt': countd})



def tous_livres(request):
      books=Livre.objects.all()
      if 'Search' in request.GET: 
            Search=request.GET['Search']
            if Search=="":
                  books
            else:
                  books=Livre.objects.filter(titre = Search, auteur= Search)

      # countd = Livre.objects.count(),'countdt': countd
      return render(request,"livre/livres.html",{'books':books})

def create_livre(request):
      form=LivreForm
      if request.method == 'POST':
            form=LivreForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/livres')  # 4
      else:
       return render(request,"livre/new_book.html",{'form':form})

# def update_emplacement(request,pk):
#       aut_data=get_object_or_404(Emplacement, id=pk)
#       form=EmplacementForm(instance=aut_data)
#       if request.method == 'POST':
#             form=EmplacementForm(request.POST,instance=aut_data)
#             if form.is_valid():
#                   form.save()
#             return redirect('/emplacements')  # 4
#       else:
#        return render(request,"emplacement/update_emplacement.html",{'form':form})
   
   
# def update_compartimelivre(request,id):
#       etgr_data=Livre.objects.get(Id=id)
#       form=LivreForm(instance=etgr_data)
#       if request.method == 'POST':
#             form=LivreForm(request.POST,instance=etgr_data)
#             if form.is_valid():
#                   form.save()
#             return redirect('/livres')  # 4
#       else:
#        return render(request,"livre/update_book.html",{'form':form})   

   
def update_book(request,pk):
      etgr_data=Livre.objects.get(id=pk)
      form=LivreForm(instance=etgr_data)
      if request.method == 'POST':
            form=LivreForm(request.POST,instance=etgr_data)
            if form.is_valid():
                  form.save()
            return redirect('/livres')  # 4
      else:
       return render(request,"livre/update_book.html",{'form':form})   

# def delete_emplacement(request,Id):
#       aut_data=Livre.objects.get(id=Id)
#       aut_data.delete()
#       return redirect('/livres')

def delete_livre(request,Id):
      aut_data=Livre.objects.get(id=Id)
      aut_data.delete()
      return redirect('/livres')