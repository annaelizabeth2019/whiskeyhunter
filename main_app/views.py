from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Whiskey
from .forms import TastingForm

class WhiskeyCreate(CreateView):
  model = Whiskey
  fields = '__all__'
  success_url = '/whiskey/'

class WhiskeyUpdate(UpdateView):
  model = Whiskey
  fields = '__all__'

class WhiskeyDelete(DeleteView):
  model = Whiskey
  success_url = '/whiskey/'

def home(request):
  return render(request, 'home.html', { 'bodyclass' : "home" })

def about(request):
  return render(request, 'about.html')

def whiskey_index(request):
  whiskey = Whiskey.objects.all()
  return render(request, 'whiskey/index.html', { 'whiskey': whiskey })

def whiskey_detail(request, whiskey_id):
  whiskey = Whiskey.objects.get(id=whiskey_id)
  tasting_form = TastingForm()
  return render(request, 'whiskey/detail.html', {
    'whiskey': whiskey, 'tasting_form': tasting_form
  })

def add_tasting(request, whiskey_id):
  form = TastingForm(request.POST)
  if form.is_valid():
    new_tasting = form.save(commit=False)
    new_tasting.whiskey_id = whiskey_id
    new_tasting.save()
  return redirect('detail', whiskey_id=whiskey_id)