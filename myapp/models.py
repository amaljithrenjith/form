from django.db import models

# Create your models here.
# Note that I have used an uppercase letter for class name

class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.CharField(max_length=120)
  desc = models.TextField()
  date = models.DateField()


  def __str__(self):
    return self.name


