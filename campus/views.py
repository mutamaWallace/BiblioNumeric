

from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Campus
from .forms import CampusForm
# Create your views here.


def all_campuses(request):
      campus_data=Campus.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  campus_data
            else:
                  campus_data=Campus.objects.filter(nom =Search)

      countdt = Campus.objects.count()
      return render(request,"campus/cmpus.html",{'campus_data':campus_data,'countdt': countdt})

def create_campus(request):
      form=CampusForm
      if request.method == 'POST':
            form=CampusForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/campuses')  # 4
      else:
       return render(request,"campus/new_campus.html",{'form':form})

def update_campus(request,Id):
      aut_data=Campus.objects.get(id=Id)
      form=CampusForm(instance=aut_data)
      if request.method == 'POST':
            form=CampusForm(request.POST,instance=aut_data)
            if form.is_valid():
                  form.save()
            return redirect('/campuses')  # 4
      else:
       return render(request,"campus/update_campus.html",{'form':form})

def delete_campus(request,Id):
      aut_data=Campus.objects.get(id=Id)
      aut_data.delete()
      return redirect('/campuses')    