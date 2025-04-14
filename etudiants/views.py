
# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Etudiants
from .forms import EtudiantsForm

def all_student(request):
      students_data=Etudiants.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  students_data
            else:
                  students_data=Etudiants.objects.filter(titre = Search)

      countd = Etudiants.objects.count()
      return render(request,"etudiants/all_student.html",{'students_data': students_data,'countdt': countd})

def emprunt_book_to_student(request):
      form=EtudiantsForm
      if request.method == 'POST':
            form=EtudiantsForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/students')  # 4
      else:
       return render(request,"etudiants/new_emprunt_to_student.html",{'form':form})

   

def update_student(request,pk):
      student_data=Etudiants.objects.get(id=pk)
      form=EtudiantsForm(instance=student_data)
      if request.method == 'POST':
            form=EtudiantsForm(request.POST,instance=student_data)
            if form.is_valid():
                  form.save()
            return redirect('/students')  # 4
      else:
       return render(request,"etudiants/update_etudiant.html",{'form':form})   


