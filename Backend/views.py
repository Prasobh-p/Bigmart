from django.shortcuts import render,redirect
from Backend.models import martdb,prodb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import ContactDB
from django.contrib import messages

# Create your views here.
def index_page(req):
    return render(req,"index.html")
def add_categ(req):
    return render(req,"AddCategory.html")

def save_categ(req):
    if req.method=="POST":
        na=req.POST.get("name")
        img=req.FILES['image']
        des=req.POST.get("desc")
        ob=martdb(Name=na,Image=img,Description=des)
        ob.save()
        messages.success(req,"added")
        return redirect(add_categ)

def display_categ(req):
    data=martdb.objects.all()
    messages.error(req,"Deleted")
    return render(req,"DisplayCategory.html",{'data':data})

def edit_categ(req,cid):
    data=martdb.objects.get(id=cid)
    return render(req,"edit_category.html",{'data':data})

def update_categ(req,cid):
    if req.method=="POST":
        na=req.POST.get("name")
        des=req.POST.get("desc")
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except:
            file=martdb.objects.get(id=cid).Image
    martdb.objects.filter(id=cid).update(Image=file,Name=na,Description=des)
    return redirect(display_categ)

def delete_categ(req,cid):
    data=martdb.objects.filter(id=cid)
    data.delete()
    return redirect(display_categ)

def admin(req):
    return render(req,"Login.html")

def admin_login(req):
    if req.method=="POST":
        un=req.POST.get("username")
        pas=req.POST.get("pass")
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pas)
            if x is not None:
                login(req,x)
                req.session['username']=un
                req.session['password']=pas
                messages.success(req,"welcome..")
                return redirect(index_page)
            else:
                messages.warning(req, 'invalid username or password ')
                return redirect(admin)
        else:
            messages.warning(req, 'invalid username or password')
            return redirect(admin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin)

def add_prod(req):
    data=martdb.objects.all()
    return render(req,"AddProducts.html",{'data':data})

def save_prod(req):
    if req.method=="POST":
        cna=req.POST.get("cname")
        pna=req.POST.get("pname")
        pr=req.POST.get("price")
        img=req.FILES['image']
        des=req.POST.get("desc")
        ob1=prodb(CatName=cna,Name=pna,Price=pr,Image=img,Description=des)
        ob1.save()
        return redirect(add_prod)

def display_pro(req):
    data=prodb.objects.all()
    return render(req,"DisplayProduct.html",{'data':data})

def edit_pro(req,pid):
    data=prodb.objects.get(id=pid)
    cat=martdb.objects.all()
    return render(req,"edit_product.html",{'data':data,'cat':cat})

def update_pro(req,pid):
    if req.method=="POST":
        cna = req.POST.get("cname")
        pna = req.POST.get("pname")
        pr = req.POST.get("price")
        des=req.POST.get("desc")
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except:
            file=prodb.objects.get(id=pid).Image
    prodb.objects.filter(id=pid).update(CatName=cna,Name=pna,Price=pr,Image=file,Description=des)
    return redirect(display_pro)

def delete_pro(req,pid):
    data=prodb.objects.filter(id=pid)
    data.delete()
    return redirect(display_pro)

def contact_details(req):
    data=ContactDB.objects.all()
    return render(req,"contactdata.html",{'data':data})




