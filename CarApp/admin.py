from django.contrib import admin

# Register your models here.
from .models import Logintable, ProductTable, CustomerTable, Showroom, category, CustomerFeedBack

admin.site.register(Logintable)
admin.site.register(ProductTable)
admin.site.register(CustomerTable)
admin.site.register(Showroom)
admin.site.register(category)
admin.site.register(CustomerFeedBack)
