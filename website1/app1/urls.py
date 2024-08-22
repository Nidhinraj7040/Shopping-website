from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('products',views.products,name='products'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('account',views.account,name='account'),
    path('logout',views.logout,name='logout'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('products',views.products,name='products'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('cart',views.cart,name='cart'),
    path('addtowish/<int:id>',views.addtowish,name='addtowish'),
    path('wishlist',views.wishlist,name='wishlist'),
    #path('helpcenter',views.helpcenter,name='helpcenter'),

    path('checkout',views.checkout,name='checkout'),
    path('myorders',views.myorders,name='myorders'),
    path('confirmorder',views.confirmorder,name='confirmorder'),


   

    # for admin page
    path('dashboard',views.dashboard,name='contacts'),
    path('contacts',views.contacts,name='contacts'),
    path('registrationadmin',views.registrationadmin,name='registrationadmin'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('admincategory',views.admincategory,name='admincategory'),
    path('adminproducts',views.adminproducts,name='adminproducts'),
    path('editproduct/<int:id>',views.editproduct,name='editproduct'),
    path('editcategory/<int:id>',views.editcategory,name='editcategory'),
    path('adminlogin',views.adminlogin,name='adminlogin'), 
    path('adminlogout',views.adminlogout,name='adminlogout'), 
    path('addnotify',views.addnotify,name='addnotify'), 

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)