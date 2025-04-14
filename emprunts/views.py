
# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Emprunt
from .forms import EmpruntForm

def all_emprunts(request):
      emprunt_data=Emprunt.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  emprunt_data
            else:
                  emprunt_data=Emprunt.objects.filter(titre = Search)

      countd = Emprunt.objects.count()
      return render(request,"emprunt/all_emprunts.html",{'emprunt_data': emprunt_data,'countdt': countd})

def add_emprunt(request):
      form=EmpruntForm
      if request.method == 'POST':
            form=EmpruntForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/emprunts')  # 4
      else:
       return render(request,"emprunt/new_emprunt.html",{'form':form})

   

def update_emprunt(request,pk):
      student_data=Emprunt.objects.get(id=pk)
      form=EmpruntForm(instance=student_data)
      if request.method == 'POST':
            form=EmpruntForm(request.POST,instance=student_data)
            if form.is_valid():
                  form.save()
            return redirect('/emprunts')  # 4
      else:
       return render(request,"emprunt/update_emprunt.html",{'form':form})   


