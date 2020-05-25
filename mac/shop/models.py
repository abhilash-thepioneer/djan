from django.db import models
from django.contrib.auth.models import User as uu
from django.db.models.signals import pre_delete

# Create your models here.
class Productnew(models.Model):
	product_id = models.AutoField
	product_name = models.CharField(max_length=50)
	category=models.CharField(max_length=50,default="")
	sub_category=models.CharField(max_length=50,default="")
	price=models.IntegerField(default=0)
	desc = models.CharField(max_length=300)
	product_date = models.DateField()
	image=models.ImageField(upload_to="shop/images",default="")
	seller=models.ForeignKey(uu,default=None,on_delete=models.CASCADE)

	def __str__(self):
		return self.product_name


class Contact(models.Model):
	# = models.AutoField
	msd_id=models.AutoField(primary_key=True)
	name= models.CharField(max_length=50,default="")
	email=models.CharField(max_length=50,default="")
	phone=models.CharField(max_length=50,default="")
	desc=models.CharField(max_length=50,default="")
	buyer=models.ForeignKey(uu,default=None,on_delete=models.CASCADE)


class Orders(models.Model):
	order_id=models.AutoField(primary_key=True)
	items_json=models.CharField(max_length=50,default="")
	amount=models.IntegerField(default=0)
	name=models.CharField(max_length=50,default="")
	email=models.CharField(max_length=50,default="")
	address=models.CharField(max_length=111,default="")
	city=models.CharField(max_length=50,default="")
	state=models.CharField(max_length=50,default="")
	zip_code=models.CharField(max_length=50,default="")
	phone=models.CharField(max_length=50,default="")

	def __str__(self):
		return self.name

class OrderUpdate(models.Model):
	update_id=models.AutoField(primary_key=True)
	order_id=models.IntegerField(default="")
	update_desc=models.CharField(max_length=200,default="")
	timestamp=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.update_desc[0:7]+" ..."










