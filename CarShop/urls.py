"""CarShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from CarApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage),
    path('registerpage/', views.registerpage),
    path('registerationpage/', views.registerationpage),
    path('loginpage/', views.loginpage),
    path('login/', views.login),
    path('adminpage/', views.adminpage),
    path('addproductpage/', views.addproductpage),
    path('addproducts/', views.addproducts),
    path('ProductTablePage/', views.ProductTablePage),
    path('ProductDelete/<int:id>', views.ProductDelete),
    path('ProductUpdatePage/', views.ProductUpdatePage),
    path('ProductUpdate/<int:id>', views.ProductUpdate),
    path('ProductUpdateView/<int:id>', views.ProductUpdateView),
    path('addcustomerspage/', views.addcustomerspage),
    path('addcustomer/', views.addcustomer),
    path('DeleteCustomerPage/', views.DeleteCustomerPage),
    path('DeleteCustomer/<int:id>', views.DeleteCustomer),
    path('ShowRoomTable/', views.ShowRoomTable),
    path('AddView/', views.AddView),
    path('AddShowRoom/', views.AddShowRoom),
    path('DeleteShowRoom/', views.DeleteShowRoom),
    path('DeleteRoom/<int:id>', views.DeleteRoom),
    path('UpdateShowRoomView/', views.UpdateShowRoomView),
    path('UpdateShowRoom/<int:id>', views.UpdateShowRoom),
    path('EditShowRoom/<int:id>', views.EditShowRoom),
    path('CustomerProductsPage/', views.CustomerProductsPage),
    path('ProfileCustomer/', views.ProfileCustomer),
    path('CustomerHome/', views.CustomerHome),
    path('ShowRoomProductsPage/', views.ShowRoomProductsPage),
    path('ShowRoomProductAdd/', views.ShowRoomProductAdd),
    path('ShowroomAddProducts/', views.ShowroomAddProducts),
    path('ShowRoomHomePage/', views.ShowRoomHomePage),
    path('ShowRoomProductDelete/<int:id>', views.ShowRoomProductDelete),
    path('ShowRoomProductEdit/<int:id>', views.ShowRoomProductEdit),
    path('ShowRoomProductEditPage/<int:id>', views. ShowRoomProductEditPage),
    path('ShowRoomProfilePage/', views.ShowRoomProfilePage),
    path('AdminAddCategory/', views.AdminAddCategory),
    path('AdminAddCategoryPage/', views.AdminAddCategoryPage),
    path('CustomerCategorySelect/<int:id>', views.CustomerCategorySelect),
    path('CustomerFeedBackPage/', views.CustomerFeedBackPage),
    path('CustomerFeedBackAdd/', views.CustomerFeedBackAdd),
    path('AdminFeedBacks/', views.AdminFeedBacks),
    path('ShowRoomCategory/<int:id>', views.ShowRoomCategory),
    path('SortProducts/', views.SortProducts),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)