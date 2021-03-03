from django.db import models
# Create your models here.
class Logintable(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    type = models.CharField(max_length=200)
    class Meta:
        db_table = 'Logintable'
class ProductTable(models.Model):
    ProductNo = models.IntegerField()
    ProductName = models.CharField(max_length=300)
    Color = models.CharField(max_length=300)
    Price = models.IntegerField()
    category_name = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    sname = models.CharField(max_length=300)
    class Meta:
        db_table = 'ProductTable'
class CustomerTable(models.Model):
    CustomerNo = models.IntegerField()
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    address = models.CharField(max_length=400)
    Phone = models.CharField(max_length=400)
    email = models.EmailField()
    type = models.CharField(max_length=300)
    class Meta:
        db_table = 'CustomerTable'
class Showroom(models.Model):
    sno = models.IntegerField()
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    OpeningTime = models.CharField(max_length=300)
    ClosingTime = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.EmailField()
    type = models.CharField(max_length=300)
    class Meta:
        db_table = 'Showroom'
class category(models.Model):
    category_no = models.IntegerField()
    category_name = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    class Meta:
        db_table = 'category'
class CustomerFeedBack(models.Model):
    cname = models.CharField(max_length=300)
    feedback = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'CustomerFeedBack'
