from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Service(models.Model):
    service = models.CharField(max_length=256)

    def __str__(self):
        return self.service

class phone(models.Model):
    image = CloudinaryField('image')
    title  = models.CharField(max_length=256)
    Description = models.TextField()
    service = models.ForeignKey(Service,on_delete=models.PROTECT,null=True ,blank=True)
    permission = models.BooleanField(default=False)
    price = models.IntegerField()

    @property
    def discounted_price(self):
        return self.price-(self.price*5)/100

    def __str__ (self):
        return self.title
    
class contact_us(models.Model):
      First_name = models.CharField(max_length=255)
      Last_name = models.CharField(max_length=255)
      Contact_no = models.IntegerField()
      Email_id = models.EmailField()
      Message = models.TextField()

      def __str__(self):
          return self.First_name

class profileimage(models.Model):
     image = CloudinaryField('image')
     nimg  = models.CharField(max_length=266)


class Types(models.Model):
    types = models.CharField(max_length=256)

    def __str__(self):
        return self.types

class Apple(models.Model):
    image = CloudinaryField('image')
    title  = models.CharField(max_length=256)
    Description = models.TextField()
    types = models.ForeignKey(Types,on_delete=models.PROTECT,null=True ,blank=True)
    price =models.IntegerField()

    @property
    def discounted_price(self):
        return self.price-(self.price*7)/100


    def __str__ (self):
        return self.title
    