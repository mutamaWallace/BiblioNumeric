# from ast import NameConstant
from multiprocessing import context
from django.shortcuts import render,redirect


from .models import Compartiment
from .forms import CompartimentForm

# Create your views here.


# def all_compart(request):
#       compart_data=Compartiment.objects.all()
#       if 'Search' in request.GET:
            
#             Search=request.GET['Search']
#             if Search=="":
#                   compart_data
#             else:
                  
#                   compart_data=Compartiment.objects.filter(nom =Search)
      
#       countdt = Compartiment.objects.count()
#       return render(request,"compartiment/compart.html",{'countdt': countdt})
  
  
  
def all_etagere(request):
      etgr_data=Compartiment.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  etgr_data
            else:
                  etgr_data=Compartiment.objects.filter(nom =Search)

      countdt = Compartiment.objects.count()
      return render(request,"compartiment/compart.html",{'etgr_data':etgr_data,'countdt': countdt})
  
  
  
  
  
  
  
  
def create_compart(request):
      form=CompartimentForm
      if request.method == 'POST':
            form=CompartimentForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/compart')  # 4
      else:
       return render(request,"compartiment/create.html",{'form':form})
     
     
       

def delete_compart(request,Id):
      aut_data=Compartiment.objects.get(id=Id)
      aut_data.delete()
      return redirect('/compart')

def update_compartiment(request,id):
      etgr_data=Compartiment.objects.get(id=id)
      form=CompartimentForm(instance=etgr_data)
      if request.method == 'POST':
            form=CompartimentForm(request.POST,instance=etgr_data)
            if form.is_valid():
                  form.save()
            return redirect('/compart')  # 4
      else:
       return render(request,"compartiment/update.html",{'form':form})

