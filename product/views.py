# from ast import NameConstant
from multiprocessing import context
from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import product
from .forms import productForm

# Create your views here.

from django.http import HttpResponseForbidden
@login_required
def home(request):
      
      if not request.user.is_staff: 
            return HttpResponseForbidden("🚫 Accès réservé aux membres du staff.")
      pro_data=product.objects.all()[:3]
      if 'Search' in request.GET:
            
            
            Search=request.GET['Search']
      
            if Search=="":
                  
                  pro_data
            else:
                  pro_data=product.objects.filter(nom =Search)
                  
            
            
      return render(request,"product/home.html",{'prodata':pro_data})


@login_required   
def book(request):
      pro_data=product.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  pro_data
            else:
                  
                  pro_data=product.objects.filter(nom =Search)
      
      countdt = product.objects.count()
      return render(request,"product/book.html",{'countdt': countdt})

@login_required
def create(request):
      form=productForm
      if request.method == 'POST':
            form=productForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/books')  # 4
      else:
       return render(request,"product/create.html",{'form':form})


@login_required     
def delete(request,id):
      pro_data=product.objects.get(id=id)
      pro_data.delete()
      return redirect('/books')


@login_required   
def update(request,id):
      pro_data=product.objects.get(id=id)
      form=productForm(instance=pro_data)
      if request.method == 'POST':
            form=productForm(request.POST,instance=pro_data)
            if form.is_valid():
                  form.save()
            return redirect('/books')  # 4
      else:
       return render(request,"product/update.html",{'form':form})

