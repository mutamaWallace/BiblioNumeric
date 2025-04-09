
# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Universite, Faculte, Departement, Class
from .forms import UniversiteForm, FaculteForm, DepartimentForm, ClassForm

# Create your views here.


def all_universities(request):
      universite_data=Universite.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  universite_data
            else:
                  universite_data=Universite.objects.filter()

      countd = Universite.objects.count()
      return render(request,"universite/all_universities.html",{'universite_data': universite_data,'countdt': countd})

def create_universite(request):
      form=UniversiteForm
      if request.method == 'POST':
            form=UniversiteForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/universities')  # 4
      else:
       return render(request,"universite/new_universite.html",{'form':form})   
   
def update_universite(request,pk):
      univer_data=Universite.objects.get(id=pk)
      form=UniversiteForm(instance=univer_data)
      if request.method == 'POST':
            form=UniversiteForm(request.POST,instance=univer_data)
            if form.is_valid():
                  form.save()
            return redirect('/universities')  # 4
      else:
       return render(request,"universite/update_universite.html",{'form':form})   

def delete_universite(request,Id):
      aut_data=Universite.objects.get(id=Id)
      aut_data.delete()
      return redirect('/universities')
  
  
  
def all_faculties(request):
      facult_data=Faculte.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  facult_data
            else:
                  facult_data=Faculte.objects.filter()

      countd = Faculte.objects.count()
      return render(request,"faculte/all_faculties.html",{'facult_data': facult_data,'countdt': countd})

def create_faculte(request):
      form=FaculteForm
      if request.method == 'POST':
            form=FaculteForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/faculties')  # 4
      else:
       return render(request,"faculte/new_faculty.html",{'form':form})   
   
def update_faculte(request,pk):
      facult_data=Faculte.objects.get(id=pk)
      form=FaculteForm(instance=facult_data)
      if request.method == 'POST':
            form=FaculteForm(request.POST,instance=facult_data)
            if form.is_valid():
                  form.save()
            return redirect('/faculties')  # 4
      else:
       return render(request,"faculte/update_faculte.html",{'form':form})   

def delete_faculte(request,Id):
      aut_data=Faculte.objects.get(id=Id)
      aut_data.delete()
      return redirect('/faculties')
  
  
def all_departements(request):
      depart_data=Departement.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  depart_data
            else:
                  depart_data=Departement.objects.filter()

      countd = Departement.objects.count()
      return render(request,"departement/all_departs.html",{'depart_data': depart_data,'countdt': countd})

def create_departement(request):
      form=DepartimentForm
      if request.method == 'POST':
            form=DepartimentForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/departements')  # 4
      else:
       return render(request,"departement/new_depart.html",{'form':form})   
   
def update_departement(request,pk):
      facult_data=Departement.objects.get(id=pk)
      form=DepartimentForm(instance=facult_data)
      if request.method == 'POST':
            form=DepartimentForm(request.POST,instance=facult_data)
            if form.is_valid():
                  form.save()
            return redirect('/departements')  # 4
      else:
       return render(request,"departement/update_depart.html",{'form':form})   

def delete_departement(request,Id):
      aut_data=Departement.objects.get(id=Id)
      aut_data.delete()
      return redirect('/departements')
  
  
  
 
def all_classes(request):
      niveau_data=Class.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  niveau_data
            else:
                  niveau_data=Class.objects.filter()

      countd = Class.objects.count()
      return render(request,"classe/all_classes.html",{'niveau_data': niveau_data,'countdt': countd})

def create_class(request):
      form=ClassForm
      if request.method == 'POST':
            form=ClassForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/niveaux')  # 4
      else:
       return render(request,"classe/new_class.html",{'form':form})   
   
def update_class(request,pk):
      facult_data=Class.objects.get(id=pk)
      form=ClassForm(instance=facult_data)
      if request.method == 'POST':
            form=ClassForm(request.POST,instance=facult_data)
            if form.is_valid():
                  form.save()
            return redirect('/niveaux')  # 4
      else:
       return render(request,"classe/update_class.html",{'form':form})   

def delete_class(request,Id):
      aut_data=Class.objects.get(id=Id)
      aut_data.delete()
      return redirect('/niveaux')