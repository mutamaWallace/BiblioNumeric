

from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Etagere
from .forms import EtagereForm
# Create your views here.


def all_etagere(request):
      etgr_data=Etagere.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  etgr_data
            else:
                  etgr_data=Etagere.objects.filter(nom =Search)

      countdt = Etagere.objects.count()
      return render(request,"etagere/etgr.html",{'etgr_data':etgr_data,'countdt': countdt})

def create_etagere(request):
      form=EtagereForm
      if request.method == 'POST':
            form=EtagereForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/etageres')  # 4
      else:
       return render(request,"etagere/new_etagere.html",{'form':form})

def update_etagere(request,Id):
      aut_data=Etagere.objects.get(id=Id)
      form=EtagereForm(instance=aut_data)
      if request.method == 'POST':
            form=EtagereForm(request.POST,instance=aut_data)
            if form.is_valid():
                  form.save()
            return redirect('/etageres')  # 4
      else:
       return render(request,"etagere/update_etagere.html",{'form':form})

def delete_etagere(request,Id):
      aut_data=Etagere.objects.get(id=Id)
      aut_data.delete()
      return redirect('/etageres')    