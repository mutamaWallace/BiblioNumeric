
# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Etudiants
from .forms import EtudiantsForm

def all_students(request):
      students_data=Etudiants.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  students_data
            else:
                  students_data=Etudiants.objects.filter(titre = Search)

      countd = Etudiants.objects.count()
      return render(request,"etudiant/all_student.html",{'students_data': students_data,'countdt': countd})

def emprunt_book_to_student(request):
      form=EtudiantsForm
      if request.method == 'POST':
            form=EtudiantsForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/etudiants')  # 4
      else:
       return render(request,"etudiant/new_emprunt_to_student.html",{'form':form})

   

def update_student(request,pk):
      student_data=Etudiants.objects.get(id=pk)
      form=EtudiantsForm(instance=student_data)
      if request.method == 'POST':
            form=EtudiantsForm(request.POST,instance=student_data)
            if form.is_valid():
                  form.save()
            return redirect('/etudiants')  # 4
      else:
       return render(request,"etudiant/update_etudiant.html",{'form':form})   


