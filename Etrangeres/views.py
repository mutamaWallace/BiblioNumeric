
# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Etrangere
from .forms import EtrangereForm

def tous_etrangeres(request):
      etranger_data=Etrangere.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  etranger_data
            else:
                  etranger_data=Etrangere.objects.filter()

      countd = Etrangere.objects.count()
      return render(request,"etrangere/tous_etrangeres.html",{'etranger_data': etranger_data,'countdt': countd})

def create_etrangere(request):
      form=EtrangereForm
      if request.method == 'POST':
            form=EtrangereForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/etrangeres')  # 4
      else:
       return render(request,"etrangere/new_etrangere.html",{'form':form})

   

def update_etrangere(request,pk):
      etranger_data=Etrangere.objects.get(id=pk)
      form=EtrangereForm(instance=etranger_data)
      if request.method == 'POST':
            form=EtrangereForm(request.POST,instance=etranger_data)
            if form.is_valid():
                  form.save()
            return redirect('/etrangeres')  # 4
      else:
       return render(request,"etrangere/update_etrangere.html",{'form':form})   


