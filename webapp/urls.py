from django.urls import path
from webapp import views


urlpatterns=[
    path('home/',views.homepage,name="homepage"),
    path('about/',views.aboutpage,name="about"),
    path('our_products/',views.our_products,name="our_products"),
    path('contact/',views.contactpage,name="contactpage"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path ('singleproductpage/<int:pro_id>/',views.singleproductpage,name="singleproductpage"),
    path('filtered_product/<cat>/',views.filtered_product,name="filtered_product"),
    path('Register_page/',views.Register_page,name="Register_page"),
    path('Userlogin/',views.Userlogin,name="Userlogin"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('Cart/',views.Cart,name="Cart"),
    path('Cartpage/',views.Cartpage,name="Cartpage"),
    path('cartremoveiteam/<int:caid>/', views.cartremoveiteam, name="cartremoveiteam"),
    path('userloginpage/',views.userloginpage,name="userloginpage"),




]