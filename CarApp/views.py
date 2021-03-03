from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .filters import ProductTableFilter
# Create your views here.
from .models import Logintable, ProductTable, CustomerTable, Showroom, category, CustomerFeedBack


def indexpage(request):
    return render(request, 'index1.html')
def registerpage(request):
    return render(request, 'reg.html')
def registerationpage(request):
    r = Logintable()
    #r.name = request.POST.get("name")
    r.username = request.POST.get("username")
    r.password = request.POST.get("password")
    r.type = "admin"
    r.save()
    #r.confirm_password = request.POST.get("ConfirmPassword")
    #type = "customer"
    #if r.password == r.confirm_password:
    #else:
     #   return HttpResponse("Wrong password")
    return render(request, 'reg.html')

def loginpage(request):
    lg = Logintable()
    lg.username = request.POST.get("username")
    lg.password = request.POST.get("password")
    return render(request, 'login.html')
def login(request):
    if request.method == 'POST':
        data = Logintable.objects.all()
        username = request.POST.get("username")
        password = request.POST.get("password")
        flag = 0
        for i in data:
            if username == i.username and password == i.password:
                flag = 1
                type = i.type
                request.session['uid'] = username
                if type == "admin":
                    return render(request, 'index.html')
                if type == "customer":
                    return render(request, 'CustomerHomePage.html')
                if type == "showroom":
                    return render(request, 'ShowRoomHomePage.html')

        if flag == 0:
            return HttpResponse("user does not exist")

def adminpage(request):
    return render(request, 'index.html')

def addproductpage(request):
    sr = Showroom.objects.all()
    pd = category.objects.all()
    context = {'srr': sr, 'pdd': pd}
    return render(request, 'AddProducts.html', context)
def addproducts(request):
    add = ProductTable()
    add.ProductNo = request.POST.get("ProductNo")
    add.ProductName = request.POST.get("ProductName")
    add.Color = request.POST.get("Color")
    add.Price = request.POST.get("Price")
    add.category_name = request.POST.get("cname")
    add.sname = request.POST.get("sname")
    photo = request.FILES['image']
    img = FileSystemStorage()
    filename = img.save(photo.name, photo)
    upload_file_url = img.url(filename)
    add.image = upload_file_url
    add.save()
    return redirect('/adminpage')


def ProductTablePage(request):
    dt = ProductTable.objects.all()
    dpf = ProductTableFilter(request.GET, queryset=dt)
    context = {'del': dt, 'dpf': dpf}
    return render(request, 'ProductTables.html', context)
def ProductDelete(request, id):
    pd = ProductTable.objects.get(id=id)
    pd.ProductNo = request.POST.get("ProductNo")
    pd.ProductName = request.POST.get("ProductName")
    pd.color = request.POST.get("Color")
    pd.Price = request.POST.get("Price")
    pd.category_name = request.POST.get("category_name")
    pd.sname = request.POST.get("sname")
    pd.image = request.POST.get("image")
    pd.delete()
    return redirect('/ProductTablePage')
def ProductUpdatePage(request):
    pup = ProductTable.objects.all()
    puf = ProductTableFilter(request.GET, queryset=pup)
    context = {'pup': pup, 'puf': puf}
    return render(request, 'UpdateTable.html', context)
def ProductUpdate(request, id):
    pu = ProductTable.objects.get(id=id)
    pu.ProductNo = request.POST.get("ProductNo")
    pu.ProductName = request.POST.get("ProductName")
    pu.Color = request.POST.get("Color")
    pu.Price = request.POST.get("Price")
    pu.category_name = request.POST.get("category_name")
    pu.sname = request.POST.get("sname")
    photo = request.FILES['image']
    img = FileSystemStorage()
    filename = img.save(photo, photo.name)
    upload_file_url = img.url(filename)
    pu.image = upload_file_url
    pu.save()
    return redirect('/adminpage')
def ProductUpdateView(request, id):
    pv = ProductTable.objects.get(id=id)
    return render(request, 'UpdateProducts.html', {'up': pv})
def addcustomerspage(request):
    return render(request, 'AddCustomers.html')
def addcustomer(request):
    ad = CustomerTable()
    ad.username = request.POST.get("username")
    ad.password = request.POST.get("password")
    ad.CustomerNo = request.POST.get("CustomerNo")
    ad.Phone = request.POST.get("Phone")
    ad.email = request.POST.get("email")
    ad.address = request.POST.get("address")
    ad.save()
    log = Logintable()
    log.username = request.POST.get("username")
    log.password = request.POST.get("password")
    log.type = "customer"
    log.save()
    return redirect('/adminpage')
def DeleteCustomerPage(request):
    dcp = CustomerTable.objects.all()
    return render(request, 'DeleteCustomerPage.html', {'dc': dcp})
def DeleteCustomer(request, id):
    dd = CustomerTable.objects.get(id=id)
    dd.CustomerNo = request.POST.get("CustomerNo")
    dd.username = request.POST.get("username")
    dd.address = request.POST.get("address")
    dd.Phone = request.POST.get("Phone")
    dd.email = request.POST.get("email")
    dd.delete()
    return redirect('/DeleteCustomerPage')

def ShowRoomTable(request):
    srt = Showroom.objects.all()
    return render(request, 'ShowRoomTable.html', {'st': srt})
def AddShowRoom(request):
    asr = Showroom()
    asr.sno = request.POST.get("sno")
    asr.username = request.POST.get("username")
    asr.password = request.POST.get("password")
    asr.location = request.POST.get("location")
    asr.OpeningTime = request.POST.get("ot")
    asr.ClosingTime = request.POST.get("ct")
    asr.phone = request.POST.get("phone")
    asr.email = request.POST.get("email")
    asr.save()
    ar = Logintable()
    ar.username = request.POST.get("username")
    ar.password = request.POST.get("password")
    ar.type = "showroom"
    ar.save()
    return redirect('/AddView')
def AddView(request):
    return render(request, 'AddShowRooms.html')
def DeleteShowRoom(request):
    dsr = Showroom.objects.all()
    return render(request, 'DeleteShowRoom.html', {'dr': dsr})
def DeleteRoom(request, id):
    dr = Showroom.objects.get(id=id)
    dr.sno = request.POST.get("sno")
    dr.username = request.POST.get("username")
    dr.location = request.POST.get("location")
    dr.OpeningTime = request.POST.get("ot")
    dr.ClosingTime = request.POST.get("ct")
    dr.phone = request.POST.get("phone")
    dr.email = request.POST.get("email")
    dr.delete()
    return redirect('/DeleteShowRoom')

def UpdateShowRoom(request, id):
    usr = Showroom.objects.get(id=id)
    return render(request, 'ShowRoomEditPage.html', {'us': usr})
def UpdateShowRoomView(request):
    usv = Showroom.objects.all()
    return render(request, 'EditShowRoom.html', {'view': usv})
def EditShowRoom(request, id):
    es = Showroom.objects.get(id=id)
    es.sno = request.POST.get("sno")
    es.username = request.POST.get("username")
    es.location = request.POST.get("location")
    es.OpeningTime = request.POST.get("ot")
    es.ClosingTime = request.POST.get("ct")
    es.phone = request.POST.get("phone")
    es.email = request.POST.get("email")
    es.save()
    return redirect('/UpdateShowRoomView')

def CustomerProductsPage(request):
    cpp = ProductTable.objects.all()
    cpc = category.objects.all()
    st = Showroom.objects.all()
    ptf = ProductTableFilter(request.GET, queryset=cpp)
    context = {'cp': cpp, 'cpc': cpc, 'st': st, 'ptf': ptf}
    return render(request, 'CustomerProducts.html', context)
def ProfileCustomer(request):
    pro = CustomerTable.objects.all()
    cpc = category.objects.all()
    context = {'pc': pro, 'cpc': cpc}
    return render(request, 'CustomerProfiles.html', context)

def CustomerHome(request):
    cpc = category.objects.all()
    return render(request, 'CustomerHomePage.html', {'cpc': cpc})

def CustomerCategorySelect(request, id):
    ccs = category.objects.get(id=id)
    var = ccs.category_name
    cc = ProductTable.objects.filter(category_name=var)
    dd = category.objects.all()
    context = {'cc': cc, 'dd': dd}
    return render(request, 'CustomerCategorySelect.html', context)
def ShowRoomProductsPage(request):
    sp = ProductTable.objects.all()
    sd = Showroom.objects.all()
    spf = ProductTableFilter(request.GET, queryset=sp)
    context = {'sd': sd, 'sp': sp, 'spf': spf}
    return render(request, 'ShowRoomProducts.html', context)
def ShowRoomHomePage(request):
    sd = Showroom.objects.all()
    return render(request, 'ShowRoomHomePage.html', {'sd': sd})
def ShowRoomCategory(request, id):
    sn = Showroom.objects.get(id=id)
    sv = sn.username
    ps = ProductTable.objects.filter(sname=sv)
    sd = Showroom.objects.all()
    context = {'sd': sd, 'ps': ps}
    return render(request, 'ShowRoomCategory.html', context)
def ShowRoomProductAdd(request):
    sd = Showroom.objects.all()
    return render(request, 'ShowRoomProductAddPage.html', {'sd': sd})
def ShowroomAddProducts(request):
    sap = ProductTable()
    sap.ProductNo = request.POST.get("ProductNo")
    sap.ProductName = request.POST.get("ProductName")
    sap.Color = request.POST.get("Color")
    sap.Price = request.POST.get("Price")
    sap.save()
    return redirect('/ShowRoomProductsPage')
def ShowRoomProductDelete(request, id):
    spd = ProductTable.objects.get(id=id)
    spd.ProductNo = request.POST.get("ProductNo")
    spd.ProductName = request.POST.get("ProductName")
    spd.Color = request.POST.get("Color")
    spd.Price = request.POST.get("Price")
    spd.delete()
    return redirect('/ShowRoomProductsPage')

def ShowRoomProductEdit(request, id):
    sp = ProductTable.objects.get(id=id)
    sd = Showroom.objects.all()
    context = {'spp': sp, 'sd': sd}
    return render(request, 'ShowRoomProductEdit.html', context)

def ShowRoomProductEditPage(request, id):
    spe = ProductTable.objects.get(id=id)
    spe.ProductNo = request.POST.get("ProductNo")
    spe.ProductName = request.POST.get("ProductName")
    spe.Color = request.POST.get("Color")
    spe.Price = request.POST.get("Price")
    spe.save()
    return redirect('/ShowRoomProductsPage')
def ShowRoomProfilePage(request):
    srpp = Showroom.objects.all()
    return render(request, 'ShowRoomProfilePage.html', {'pro': srpp})
def AdminAddCategory(request):
    return render(request, 'AdminCategory.html')
def AdminAddCategoryPage(request):
    ac = category()
    ac.category_no = request.POST.get("cno")
    ac.category_name = request.POST.get("cname")
    photo = request.FILES['image']
    img = FileSystemStorage()
    filename = img.save(photo.name, photo)
    upload_file_url = img.url(filename)
    ac.image = upload_file_url
    ac.save()
    return render(request, 'AdminCategory.html')
def CustomerFeedBackPage(request):
    cpc = category.objects.all()
    return render(request, 'CustomerFeedBack.html', {'cpc': cpc})
def CustomerFeedBackAdd(request):
    cf = CustomerFeedBack()
    cf.cname = request.POST.get("cname")
    cf.feedback = request.POST.get("feedback")
    cf.save()
    return redirect('/CustomerFeedBackPage')
def AdminFeedBacks(request):
    af = CustomerFeedBack.objects.all()
    return render(request, 'AdminFeedbacks.html', {'af': af})
def SortProducts(request):
    sp = ProductTable.objects.order_by('Price')
    return render(request, 'SortProducts.html', {'sp': sp})