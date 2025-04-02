from django.shortcuts import render,redirect
from django.http import HttpResponse
from Backend.models import prodb,martdb
from webapp.models import ContactDB
from webapp.models import RegisterDB
from webapp.models import cartDB
from webapp.models import orderDB
from django.contrib import messages

# Create your views here.

def homepage(req):
    cat = martdb.objects.all()
    return render(req,"home.html",{'cat':cat})
def aboutpage(req):
    cat = martdb.objects.all()
    return render(req,"about.html",{'cat':cat})
def our_products(req):
    pro = prodb.objects.all()
    cat = martdb.objects.all()
    return render(req,"our_products.html", {'pro':pro,'cat':cat})
def contactpage(req):
    cat = martdb.objects.all()
    return render(req,"contact.html",{'cat':cat})


def save_contact(request):
    if request.method == "POST":
        cname = request.POST.get("name")
        ema = request.POST.get("email")
        sub = request.POST.get("subject")
        pho = request.POST.get("phone")
        mess = request.POST.get("message")
        obj = ContactDB(Name=cname, Email=ema, Subject=sub, Phone=pho, Message=mess)
        obj.save()
        return redirect('contactpage')

def singleproductpage(req,pro_id):
    data =prodb.objects.get(id=pro_id)
    cat = martdb.objects.all()

    return  render(req,"single_product.html",{'data':data,'cat':cat})


def filtered_product(req,cat):
    data = prodb.objects.filter(CatName=cat)
    cat = martdb.objects.all()
    return render(req,"product_filtered.html",{'data':data,'cat':cat})

def Register_page(req):
    return render(req,"Register.html")

def Userlogin(request):
    if request.method == "POST":
        uname = request.POST.get("UName")
        email = request.POST.get("Email")
        pas1 = request.POST.get("pass1")
        pas2 = request.POST.get("pass2")
        ob3 = RegisterDB(Name=uname,Email=email,Password=pas1,Confirmpassword=pas2)
        if RegisterDB.objects.filter(Name=uname).exists():
            messages.warning(request,"User already exists...")
        elif RegisterDB.objects.filter(Email=email).exists():
            messages.warning(request, "Email already exists...")
        else:
            ob3.save()
            messages.success(request, "Registered succesfully")
        return redirect('userloginpage')

def userloginpage(req):
    return render(req, "userlogin.html")

def login(request):
    if request.method=="POST":
        un=request.POST.get("name")
        pas=request.POST.get("psw")
        if RegisterDB.objects.filter(Name=un,Password=pas).exists():
            request.session['Name']=un
            request.session['Password'] = pas
            return redirect(homepage)
        else:
            return redirect(Register_page)
    else:
        return redirect(Register_page )

def logout(request):
    del request.session["Name"]
    del request.session["Password"]
    return redirect(homepage)


def Cart(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pname= request.POST.get("productname")
        Qut= request.POST.get("qut")
        tprice = request.POST.get("total")
        ob4 = cartDB(Uname=uname,Pname=pname,Quantity=Qut,Totalprice=tprice)
        ob4.save()
        return redirect('homepage')


def Cartpage(request):
    cdata = cartDB.objects.filter(Uname=request.session['Name'])
    total_price = 0
    shipping_charge = 0
    total_amount = 0

    for i in cdata:
        total_price += i.Totalprice

    if total_price > 500:
        shipping_charge = 50
    else:
        shipping_charge = 100

    total_amount = total_price + shipping_charge

    return render(request, "Cartpage.html", {'cdata': cdata, 'total_price': total_price,'shipping_charge': shipping_charge,'total_amount': total_amount})


def cartremoveiteam(request,caid):
    data=cartDB.objects.get(id=caid)
    data.delete()
    return redirect("Cartpage")



def checkoutpage(request):
    product=cartDB.objects.filter(Uname=request.session['Name'])
    total_price=0
    shipping_charge=0
    total_amount=0

    for i in product:
        total_price = total_price + i.Totalprice

    if shipping_charge >500:
        shipping_charge=50
    else:
        shipping_charge=100

    total_amount=total_price+shipping_charge

    return render(request,"checkoutpage.html",{'product':product,'total_price':total_price,'shipping_charge':shipping_charge,'total_amount':total_amount})

def paymentpage(req):
    return render(req,"payment.html")

def Orderdetails(request):
    if request.method == "POST":
        oname = request.session['Name']
        oemail = request.POST.get("email")
        oaddress = request.POST.get("adderss")
        omobile = request.POST.get("mobile")
        ototalprice = request.POST.get("total_price")
        obj5 = orderDB(Oname=oname, Oemail=oemail,Oaddress=oaddress,Omobile=omobile,Ototalprice=ototalprice)
        obj5.save()
        return redirect(paymentpage)








