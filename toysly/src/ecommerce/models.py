from django.db import models

class User(models.Model):
	user_id = models.CharField(primary_key=True, max_length=100)
	email_id = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)

class Buyer(models.Model):
	buyer_id = models.CharField(primary_key=True, max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=100)

def product_image_path(instance):
    # file will be uploaded to MEDIA_ROOT/'seller_documents'/seller_<id>
    return 'seller_documents/seller_{0}'.format(instance.seller_id)

class Seller(models.Model):
	seller_id = models.CharField(primary_key=True, max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	agency_name = models.CharField(max_length=100)
	approval_doc = models.FileField(upload_to=seller_id)

class Product(models.Model):
	product_id = models.CharField(primary_key=True, max_length=100)
	product_name = models.CharField(max_length=100)
	product_brand = models.CharField(max_length=100)
	product_description = models.TextField()
	product_price = models.DecimalField(max_digits=10, decimal_places=2)
	product_quantity_available = models.DecimalField(max_digits=10, decimal_places=0)
	product_rating = models.IntegerField()
	product_delivery_time = models.IntegerField()

def product_image_path(instance, image_id):
    # file will be uploaded to MEDIA_ROOT/'product_images'/product_<id>/<image_id>
    return 'product_images/product_{0}/{1}'.format(instance.product_id, image_id)

class ProductImages(models.Model):
	product_id = models.CharField(max_length=100)
	image_id = models.CharField(max_length=100)
	image = models.ImageField(upload_to=product_image_path)

class Category(models.Model):
	category_id = models.CharField(primary_key=True, max_length=100)
	category_name = models.CharField(max_length=100)

class Order(models.Model):
	order_id = models.CharField(primary_key=True, max_length=100)
	order_amount = models.DecimalField(max_digits=10, decimal_places=2)
	order_timestamp = models.DateTimeField(auto_now_add=True)
	delivery_date = models.DateField(auto_now=False, auto_now_add=False)

class Shipping_Details(models.Model):
	buyer_id = models.CharField(primary_key=True, max_length=100)
	delivery_address = models.TextField()
	delivery_city = models.CharField(max_length=100)
	delivery_state = models.CharField(max_length=100)
	delivery_country = models.CharField(max_length=100)
	delivery_pincode = models.CharField(max_length=100)

#class Payment(models.Model):
#	order_id = models.CharField(primary_key=True, max_length=100)

class Cart(models.Model):
	buyer_id = models.CharField(primary_key=True, max_length=100)
	product_id = models.CharField(max_length=100)
	cart_total = models.DecimalField(max_digits=10, decimal_places=2)