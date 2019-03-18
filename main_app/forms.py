from django.forms import ModelForm
from .models import Tasting, Whiskey

class TastingForm(ModelForm):
  class Meta:
    model = Tasting
    fields = ['date', 'rating']