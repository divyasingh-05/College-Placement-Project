from django.db import models

# Create your models here.
class Records(models.Model):
    #img=models.ImageField(upload_to ="Image/")
    name=models.CharField(max_length = 100)
    branch=models.CharField(max_length = 100)
    year=models.IntegerField()
    company=models.CharField(max_length = 200)
    package=models.FloatField()

