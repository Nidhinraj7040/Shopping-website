from django.shortcuts import render
from django.http import HttpResponse
from django. http import HttpResponseRedirect
from django.template import loader
from.models import Contact
from.models import Registration
from.models import Products
from.models import Cart
from.models import Category
from.models import Order,Wishlist, Notification
import datetime 
from.models import Adminregistration



# Create your views here.

def index(request):
    category=Category.objects.all().values()
    context={
        'category': category
    }
    Template=loader.get_template("index.html")
    return HttpResponse(Template.render(context,request))

def about(request):
    Template=loader.get_template("about.html")
    return HttpResponse(Template.render({},request))

def products(request):
    if 'catid' in request.GET:
        catid = request.GET['catid']
        pro=Products.objects.filter(pro_catid=catid)

    else :
    
        pro=Products.objects.all()
    context={
        'pro': pro,
    }
    Template=loader.get_template("products.html")
    return HttpResponse(Template.render(context,request))

def services(request):
    Template=loader.get_template("services.html")
    return HttpResponse(Template.render({},request))


def contact(request):
    if request.method == 'POST':
        cname=request.POST['contact_name']
        cemail=request.POST['contact_email']
        cmessage=request.POST['contact_msg']

        con= Contact(con_name=cname, con_email=cemail, con_message=cmessage)
        con.save()

    Template=loader.get_template("contact.html")
    return HttpResponse(Template.render({},request))


def registration(request):
    if "user" in request.session:
        return HttpResponseRedirect("/account")
    if request.method == 'POST':
        rname=request.POST['reg_name']
        remail=request.POST['reg_email']
        rusername=request.POST['reg_username']
        rpassword=request.POST['reg_password']
        rphonenumber=request.POST['reg_phonenumber']

        x= Registration(reg_name=rname,reg_email=remail,reg_username=rusername,reg_password=rpassword,reg_phonenumber=rphonenumber)
        x.save()

    template=loader.get_template("registration.html")
    return HttpResponse(template.render({},request))

def login(request):
    if "user" in request.session:
        return HttpResponseRedirect("/account")
    if request.method == 'POST':
        log_user= request.POST['log_username']
        log_pswd=request.POST['log_password']


        log = Registration.objects.filter(reg_username=log_user,reg_password=log_pswd)
        if log:
            request.session["user"]=log_user
            return HttpResponseRedirect("/account")

    template=loader.get_template("login.html")
    return HttpResponse(template.render({},request))

def account(request):
    if "user" not in request.session:
        return HttpResponseRedirect("/login")
    order =''
    pro=''
    wish=''
    noti=''
    
  
    user=request.session['user']
    if request.method == 'POST':
        rname=request.POST['profile_name']
        remail=request.POST['profile_email']
        
        reg = Registration.objects.filter(reg_username = user)[0]
        reg.reg_name = rname
        reg.reg_email = remail
        if len(request.FILES)!=0:
            reg.reg_image = request.FILES['profile_image']
        reg.save()
        return HttpResponseRedirect("/account?prof")

    if 'ord' in request.GET:
        user=request.session['user']
        order = Order.objects.filter(order_user = user)

    elif 'prof' in request.GET:
        user=request.session['user']
        pro=Registration.objects.filter( reg_username=user)

    elif 'wish' in request.GET:
       user=request.session['user']
       wish=Wishlist.objects.filter(wish_user=user)

    elif 'noti' in request.GET:
        user=request.session["user"]
        noti=Notification.objects.all()

    user=request.session['user']
    account=Registration.objects.filter(reg_username=user)
    context ={
        'account': account,
        'order':order,
        'pro':pro,
        'wish':wish,
        'noti':noti
    }
    template=loader.get_template("account.html")
    return HttpResponse(template.render(context,request))

def logout(request):
    if "user" in request.session:
        del request.session["user"]
    return HttpResponseRedirect("/login")

# dashboard

def dashboard(request):

    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    
    
    template=loader.get_template("dashboard/dashboard.html")
    return HttpResponse(template.render({},request))

def contacts(request):
    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    cons=Contact.objects.all().values()
    context= {
        'contacts' : cons
    }
    template=loader.get_template("dashboard/contacts.html")
    return HttpResponse(template.render(context,request))

def registrationadmin(request):
    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    regadmin=Registration.objects.all().values()
    context={
        'registrationadmin' : regadmin
    }

    template=loader.get_template("dashboard/registrationadmin.html")
    return HttpResponse(template.render(context,request))

def adminlogin(request):

    if request.method == 'POST':
        username = request.POST['admin_user']
        password = request.POST['admin_password'] 
        adminlogin = Adminregistration.objects.filter( admin_user=username, admin_password=password)
        if adminlogin:  
            request.session['admin'] = username
            return HttpResponseRedirect("/dashboard")
    template = loader.get_template("dashboard/adminlogin.html")    
    return HttpResponse(template.render({},request))

def adminlogout(request):
    if "admin" in request.session:
        del request.session["admin"]
        return HttpResponseRedirect("/adminlogin")

# product page 

def addproduct(request):
    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    if request.method == 'POST':
        x=request.POST['pro_name']
        y=request.POST['pro_price']
        a=request.POST['pro_category']
        z=request.FILES['pro_image']

        

        product = Products(
            pro_name=x,pro_price=y,pro_image=z,pro_catid=a)
        product.save()
    c = Category.objects.all().values()
    context= {
       'c' : c
        }

    template=loader.get_template("dashboard/addproduct.html")
    return HttpResponse(template.render(context,request))

def addtocart(request,id):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
        
    exist = Cart.objects.filter(cart_proid =id,cart_user= request.session["user"])
    if exist:
        existcart=Cart.objects.filter(cart_proid=id,cart_user=request.session["user"])[0]
        existcart.cart_qty +=1
        existcart.cart_amount = existcart.cart_qty * existcart.cart_price
        existcart.save()
    else:
        pro = Products.objects.filter(id=id)[0]
        
        cart= Cart(cart_user = request.session["user"],
                   cart_proid = pro.id,
                   cart_name = pro.pro_name,
                   cart_price = pro.pro_price,
                   cart_image = pro.pro_image,
                   cart_qty = 1,
                   cart_amount = pro.pro_price)
        
        cart.save()
    return HttpResponseRedirect("/cart")

def addtowish(request,id):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
        
    exist = Wishlist.objects.filter(wish_proid =id,wish_user= request.session["user"])
    if exist:
        pass
    else:
        pro = Products.objects.filter(id=id)[0]
        
        wish = Wishlist(wish_user = request.session["user"],
                   wish_proid = pro.id,
                   wish_name = pro.pro_name,
                   wish_price = pro.pro_price,
                   wish_image = pro.pro_image,) 
        wish.save()
    return HttpResponseRedirect("/wishlist")
    # return HttpResponseRedirect("/products")

def addnotify(request):
    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
    
    if request.method == 'POST':
       notify=request.POST['notify']
       date=datetime.datetime.now()     
       noti= Notification(noti_message=notify,noti_date=date)
       noti.save()
       return HttpResponseRedirect('/addnotify')
    template=loader.get_template("dashboard/addnotifications.html")
    return HttpResponse(template.render({},request))
        

def cart(request):
    if "user" not in request.session:
        return HttpResponseRedirect("/login")
    
    # delete cart item

    if 'del' in request.GET:
        id = request.GET['del']
        delcart = Cart.objects.filter(id=id)[0]
        delcart.delete()

    # change cart quantity

    if 'q' in request.GET:
        q = request.GET['q']
        cp = request.GET['cp'] 
        cart3 = Cart.objects.filter(id=cp)[0]  

        if q =='inc':
            cart3.cart_qty+=1
        elif q =='dec':
            if(cart3.cart_qty>1):
                cart3.cart_qty-=1
        cart3.cart_amount = cart3.cart_qty * cart3.cart_price
        cart3.save()
    user = request.session["user"]
    cart=Cart.objects.filter(cart_user=user).values()
    cart2=Cart.objects.filter(cart_user=user)

    tot=shp=gst=gtot=0
    for x in cart2:
        tot+=x.cart_amount
        shp = tot * 10/100
        gst = tot * 18/100
        gtot = tot+shp+gst

    request.session["tot"]=tot
    request.session["gst"]=gst
    request.session["shp"]=shp
    request.session["gtot"]=gtot


    context={
        'cart': cart,
        'tot' : tot,
        'shp' : shp,
        'gst' : gst,
        'gtot' : gtot,
        }
    template = loader.get_template("cart.html")
    return HttpResponse(template.render(context,request)) 

def wishlist(request):
    if "user" not in request.session:
        return HttpResponseRedirect("/login")
    user = request.session["user"]
    wishlist = Wishlist.objects.filter(wish_user=user).values()
    context = {
        'wishlist':wishlist,
    }
    template = loader.get_template("wishlist.html")
    return HttpResponse(template.render(context,request)) 
    
    
    
def addcategory(request):
    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    if request.method == 'POST':
      x=request.POST['cat_name']
      y=request.FILES['cat_image']

      category = Category(
           cat_name=x,cat_image=y)
      category.save()

    template=loader.get_template("dashboard/addcategory.html")
    return HttpResponse(template.render({},request))

# for admin

def adminproducts(request):
    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    # if 'user' not in request.session:
    #     return HttpResponseRedirect('/login')
    adminpro  = Products.objects.all()
    catnames =[]
    for x in adminpro:
        catid = x.pro_catid
        cat=Category.objects.filter(id = catid)[0]
        catname = cat.cat_name
        catnames.append(catname)
    context = {
        'adminpro':zip(adminpro,catnames)
    }
    template=loader.get_template("dashboard/adminproducts.html")
    return HttpResponse(template.render(context,request))

def admincategory(request):
    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    if 'del' in request.GET:
        id=request.GET['del']
        delcat = Category.objects.filter(id=id)[0]
        delcat.delete()
        HttpResponseRedirect("/admincategory")

    admincat = Category.objects.all().values()
    context = {
        'admincat': admincat
    }
    template=loader.get_template("dashboard/admincategory.html")
    return HttpResponse(template.render(context,request))

def editproduct(request,id):
    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    if request.method == 'POST':
        x=request.POST['edit_name']
        z=request.POST['edit_price']
        editproduct=Products.objects.filter(id = id)[0]
        editproduct.pro_name=x
        editproduct.pro_price=z
        if len(request.FILES) != 0:
            y=request.FILES['edit_image']
            editproduct.pro_image=y
        editproduct.save()
        return HttpResponseRedirect("/adminproducts")
    edit=Products.objects.filter(id=id).values()
    context={
        'edit':edit,
    }
    template=loader.get_template("dashboard/editproduct.html")
    return HttpResponse(template.render(context,request))

def editcategory(request,id):
    if 'admin' not in request.session:
       return HttpResponseRedirect("/adminlogin")
    category=Category.objects.filter(id=id).values()
    if request.method == 'POST':
        editname=request.POST['cat_name']

        updatecat=Category.objects.filter(id=id)[0]
        updatecat.cat_name=editname
        if len(request.FILES) !=0:
            editimage=request.FILES['cat_image']
            updatecat.cat_image=editimage
        updatecat.save()
        return HttpResponseRedirect("/admincategory")
    
    context={
        'category':category,
    }
    template=loader.get_template("dashboard/editcategory.html")
    return HttpResponse(template.render(context,request))
            

def checkout(request):
    if "user" not in request.session:
        return HttpResponseRedirect('/login')

    co=0
    adrs = dtype = ""

    if 'dlv_adrs' in request.POST:
        adrs = request.POST["dlv_adrs"]
        dtype = request.POST["dlv_type"]
        co = 1

    user= request.session["user"]

    older = Order.objects.filter(order_user=user,order_status=0)
    older.delete()

    cart=Cart.objects.filter(cart_user=user)
    for x in cart:
        odr = Order(order_user = x.cart_user,
                    order_name = x.cart_name,
                    order_price = x.cart_price,
                    order_image = x.cart_image,

                    order_qty = x.cart_qty,
                    order_amount = x.cart_amount,
                    order_adress = adrs,
                    order_dlvtype = dtype,
                    order_status = 0
                    )
        odr.save()

    order=Order.objects.filter(order_user=user,order_status=0).values()

    tot=request.session['tot']
    gst=request.session['gst']
    shp=request.session['shp']
    gtot=request.session['gtot']

    context={
        'order':order,
        'tot':tot,
        'shp':shp,
        'gst':gst,
        'gtot':gtot,
        'co':co
    }

    template = loader.get_template("checkout.html")
    return HttpResponse(template.render(context,request))
                    
def confirmorder(request):
    user = request.session["user"]
    order = Order.objects.filter(order_user=user,order_status=0)

    for x in order:
        x.order_status=1
        x.save()
        template=loader.get_template("confirmorder.html")
        return HttpResponse(template.render({},request))
    
def myorders(request):
    user = request.session["user"]
    order = Order.objects.filter(order_user=user,order_status=1)
    context = {
        'order' : order
    }
    template = loader.get_template("myorders.html")
    return HttpResponse(template.render(context,request))
                  














