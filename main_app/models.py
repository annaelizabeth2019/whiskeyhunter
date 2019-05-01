from django.db import models
from django.urls import reverse

RATING = (
    ('5', '⭐⭐⭐⭐⭐'),
    ('4', '⭐⭐⭐⭐'),
    ('3', '⭐⭐⭐'),
    ('2', '⭐⭐'),
    ('1', '⭐'),
)

class Whiskey(models.Model):
  name = models.CharField(max_length=200)
  brand = models.CharField(max_length=10)
  description = models.TextField(max_length=250, blank=True)
  origin = models.TextField(max_length=100, blank=True)
  SKU = models.TextField(max_length=100, blank=True, unique=True)
  type_of = models.TextField(max_length=100, blank=True)
  bottle_size = models.TextField(max_length=100, blank=True)
  image = models.TextField(blank=True)
  ABV = models.FloatField(max_length=5, blank=True, null=True)
  maturing = models.TextField(max_length=100, blank=True)
  post_treatment = models.TextField(max_length=200, blank=True)



  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'whiskey_id' : self.id})

class Tasting(models.Model):
  date = models.DateField('Tasting date')
  rating = models.CharField(
    max_length=1,
    choices=RATING,
    default=RATING[0][0]
  )
  whiskey = models.ForeignKey(Whiskey, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_rating_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']