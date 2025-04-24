from django.shortcuts import render

# Create your views here.

# from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Abonnement
from .forms import AbonnementForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def all_abonnements(request):
      abonne_data=Abonnement.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  abonne_data
            else:
                  abonne_data=Abonnement.objects.filter()

      countd = Abonnement.objects.count()
      return render(request,"abonnement/all_abonnes.html",{'abonne_data': abonne_data,'countdt': countd})


@login_required
def create_abonnee(request):
      form=AbonnementForm
      if request.method == 'POST':
            form=AbonnementForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/abonnes')  # 4
      else:
       return render(request,"abonnement/new_abonne.html",{'form':form})  
 
  
@login_required  
def update_abonne(request,pk):
      abonne_data=Abonnement.objects.get(id=pk)
      form=AbonnementForm(instance=abonne_data)
      if request.method == 'POST':
            form=AbonnementForm(request.POST,instance=abonne_data)
            if form.is_valid():
                  form.save()
            return redirect('/abonnes')  # 4
      else:
       return render(request,"abonnement/update_abonne.html",{'form':form})  
 
 
  
@login_required
def delete_abonne(request,Id):
      abonne_data=Abonnement.objects.get(id=Id)
      abonne_data.delete()
      return redirect('/abonnes')
  
  
  