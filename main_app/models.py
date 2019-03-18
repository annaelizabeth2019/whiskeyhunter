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
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  origin = models.TextField(max_length=100)
  # flavors = models.ManyToManyField(Flavor)

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