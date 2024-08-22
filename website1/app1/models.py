from django.db import models

# Create your models here.
class Contact(models.Model):

 con_name=models.CharField(max_length=255)
 con_email=models.CharField(max_length=255)
 con_message=models.TextField()
    
 def __str__(self):
    return self.con_name

class Registration(models.Model):
      reg_name=models.CharField(max_length=255)
      reg_email=models.CharField(max_length=255)
      reg_username=models.CharField(max_length=255)
      reg_password=models.CharField(max_length=255)
      reg_phonenumber=models.CharField(max_length=255)
      reg_image=models.FileField(null=True,upload_to="profile")

      def __str__(self):
        return self.reg_name 
      
class Products(models.Model):
      pro_name=models.CharField(max_length=255)
      pro_price=models.CharField(max_length=255)
      pro_image=models.FileField(null=True,upload_to="products")
      pro_catid=models.CharField(null=True,max_length=255)
    
      def __str__(self):
         return self.pro_name
 
class Cart(models.Model):
    cart_user = models.CharField(max_length=250,default=None)
    cart_proid= models.IntegerField(null=True)
    cart_name = models.CharField(max_length=250)
    cart_price = models.FloatField(max_length=250)
    cart_image = models.FileField(null=True)
    cart_qty = models.IntegerField()
    cart_amount= models.FloatField()

    def __str__(self):
       return self.cart_name    
    
class Wishlist(models.Model):
    wish_user = models.CharField(max_length=250,default=None)
    wish_proid= models.IntegerField(null=True)
    wish_name = models.CharField(max_length=250)
    wish_price = models.FloatField(max_length=250)
    wish_image = models.FileField(null=True)

    def __str__(self):
      return self.wish_name
    
class Notification(models.Model):
   noti_message = models.TextField()
   noti_date = models.DateTimeField(null=True)  
    
class Category(models.Model):
   cat_name=models.CharField(max_length=255)
   cat_image=models.FileField(null=True,upload_to="category")

   def __str__(self):
      return self.cat_name

class Order(models.Model):
   order_user = models.CharField(max_length=250,default=None)
   order_name = models.CharField(max_length=250)
   order_price = models.FloatField(max_length=250)
   order_image = models.FileField(null=True)
   order_qty = models.IntegerField()
   order_amount = models.FloatField()
   
   order_adress = models.TextField(null=True)
   order_dlvtype = models.TextField(null=True,max_length=10)
   order_status = models.IntegerField(default=0)

   def __str__(self):
      return self.order_name
   
class Adminregistration(models.Model):
   admin_user=models.CharField(max_length=255)
   admin_password=models.CharField(max_length=255)

   def __str__(self):
      return self.admin_user


   
   
      


  
  