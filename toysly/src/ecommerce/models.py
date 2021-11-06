from django.db import models
from django.contrib.auth.models import User

def seller_doc_path(instance):
    # file will be uploaded to MEDIA_ROOT/'seller_documents'/seller_<id>
    return 'seller_documents/seller_{0}'.format(instance.id)

def product_image_path(instance, image_id):
    # file will be uploaded to MEDIA_ROOT/'product_images'/product_<id>/<image_id>
    return 'product_images/product_{0}/{1}'.format(instance.product.id, instance.product_image_name)


class Buyer(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	gender = models.CharField(max_length=100)
	def __str__(self):
		return self.id+' '+self.user.first_name

class Seller(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	agency_name = models.CharField(max_length=100)
	approval_doc = models.FileField(upload_to=seller_doc_path)
	def __str__(self):
		return self.id+' '+self.user.first_name

class Product(models.Model):
	product_name = models.CharField(max_length=100)
	product_brand = models.CharField(max_length=100)
	product_description = models.TextField()
	product_price = models.DecimalField(max_digits=10, decimal_places=2)
	product_quantity_available = models.DecimalField(max_digits=10, decimal_places=0)
	product_delivery_time = models.IntegerField()
	def __str__(self):
		return str(self.id) + ' ' + self.product_name

class ProductImage(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
	product_image_name = models.CharField(max_length=100,default='0')
	image = models.ImageField(upload_to=product_image_path)
	def __str__(self):
		return str(self.id) + ' ' + str(self.product.id)

class Category(models.Model):
	category_name = models.CharField(max_length=100)
	def __str__(self):
		return self.category_name

class Order(models.Model):
	order_amount = models.DecimalField(max_digits=10, decimal_places=2)
	order_timestamp = models.DateTimeField(auto_now_add=True)
	delivery_date = models.DateField(auto_now=False, auto_now_add=False)

class Shipping_Details(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE,primary_key=True,default=None)
	delivery_address = models.TextField()
	delivery_city = models.CharField(max_length=100)
	delivery_state = models.CharField(max_length=100)
	delivery_country = models.CharField(max_length=100)
	delivery_pincode = models.CharField(max_length=100)

#class Payment(models.Model):
#	order = models.ForeignKey(Order,on_delete=models.CASCADE,default=None)

class Cart(models.Model):
	buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE,primary_key=True,default=None)
	product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
	cart_total = models.DecimalField(max_digits=10, decimal_places=2)