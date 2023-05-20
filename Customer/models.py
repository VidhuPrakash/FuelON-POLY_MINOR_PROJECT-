from django.db import models
class Fuel(models.Model):
    name = models.CharField(max_length=100,default='Petrol/diesel')
    Category=models.ManyToManyField('category',related_name='Name')
    image=models.ImageField(upload_to='menu/')
    price=models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.name
 
class category(models.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name
class order_data(models.Model):
     customer_name = models.CharField(max_length=20)
     phone= models.CharField(max_length=10)
     category=models.CharField(max_length=10,default='')
     location=models.CharField(max_length=100)
     quantity=models.CharField(max_length=3) 
     def __str__(self):
        return self.customer_name
     
class KeralaHub(models.Model):
     hub_name=models.CharField(max_length=20)
     hub_dist=models.CharField(max_length=20)
     hub_num=models.CharField(max_length=10)
     def __str__(self):
      return self.hub_name




# Create your models here.
