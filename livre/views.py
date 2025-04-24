
# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Livre
from .forms import LivreForm
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .serializers import LivreSerializer


@login_required
class LivreList(APIView):
    def get(self, request):
        livres = Livre.objects.all()
        serializer = LivreSerializer(livres, many=True)
        return Response(serializer.data)



class LivreViewSet(viewsets.ModelViewSet):
      queryset = Livre.objects.all()
      serializer_class = LivreSerializer
      
      
@login_required
def all_book(request):
      
      book_data=Livre.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  book_data
            else:
                  book_data=Livre.objects.filter(titre = Search)

      countd = Livre.objects.count()
      return render(request,"livre/all_book.html",{'book_data': book_data,'countdt': countd})

@login_required
def tous_livres(request):
      books=Livre.objects.all()
      if 'Search' in request.GET: 
            Search=request.GET['Search']
            if Search=="":
                  books
            else:
                  books=Livre.objects.filter(titre=Search, auteur=Search)

      countd = Livre.objects.count()
      return render(request,"livre/livres.html",{'books':books,'countdt': countd})
@login_required
def create_livre(request):
      form=LivreForm
      if request.method == 'POST':
            form=LivreForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request, "📘 Livre ajouté avec succès !")
                  return redirect('/livres')  # ou une autre page
            else:
                 messages.error(request, "❌ Une erreur est survenue lors de l'enregistrement.")


            return redirect('/livres')  # 4
      else:
       return render(request,"livre/new_book.html",{'form':form})


   
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


def delete_livre(request,Id):
      aut_data=Livre.objects.get(id=Id)
      aut_data.delete()
      return redirect('/livres')


