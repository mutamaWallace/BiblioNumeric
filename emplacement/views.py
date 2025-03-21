

from ast import NameConstant
from django.shortcuts import render,redirect, get_object_or_404
from .models import Emplacement
from .forms import EmplacementForm
# Create your views here.


def all_emplacement(request):
      empla_data=Emplacement.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  empla_data
            else:
                  empla_data=Emplacement.objects.filter(position_precise =Search)

      countdt = Emplacement.objects.count()
      return render(request,"emplacement/all_emplacement.html",{'etgr_data':empla_data,'countdt': countdt})



  
def all_etagere(request):
      etgr_data=Emplacement.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  etgr_data
            else:
                  etgr_data=Emplacement.objects.filter(position_precise =Search)

      countdt = Emplacement.objects.count()
      return render(request,"emplacement/all_emplacement.html",{'etgr_data':etgr_data,'countdt': countdt})
  
  
  
  





def create_emplacement(request):
      form=EmplacementForm
      if request.method == 'POST':
            form=EmplacementForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/emplacements')  # 4
      else:
       return render(request,"emplacement/new_emplacement.html",{'form':form})

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
   
   
   
def update_compartimen(request,id):
      etgr_data=Emplacement.objects.get(id=id)
      form=EmplacementForm(instance=etgr_data)
      if request.method == 'POST':
            form=EmplacementForm(request.POST,instance=etgr_data)
            if form.is_valid():
                  form.save()
            return redirect('/emplacements')  # 4
      else:
       return render(request,"emplacement/update_emplacement.html",{'form':form})   

# def delete_emplacement(request,Id):
#       aut_data=Emplacement.objects.get(id=Id)
#       aut_data.delete()
#       return redirect('/emplacements')
def delete_etager(request,Id):
      aut_data=Emplacement.objects.get(id=Id)
      aut_data.delete()
      return redirect('/emplacements')