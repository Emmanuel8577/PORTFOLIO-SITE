from django.db import models



# Create your models here.
class Contact(models.Model): 
 name = models.CharField(max_length = 200, null=False, blank=False)
 email = models.EmailField()
 mobile = models.IntegerField()
 subject = models.CharField(max_length=250)
 description = models.TextField()


 def __str__(self):
  return self.name
 



class Portfolio(models.Model):
    image = models.ImageField(upload_to='uploads/images', null=False, blank=False, default='default_image.jpg')
    name = models.CharField(max_length=200, null=False, blank=False, default='Name')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=10.0)
    category = models.CharField(max_length=100, default='category')



    def __str__(self):
     return self.name
 

class Data(models.Model):
   file=models.FileField(upload_to='myfiles/',blank=True)


   def __str__(self):
     return str(self.file)
