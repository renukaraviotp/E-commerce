from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from ecommerceapp.models import Category,Product,Customer,Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

# Create your views here.
def home(request):
    c=Category.objects.all()
    user=request.user
    
    if user.is_authenticated:
        i=Customer.objects.get(user_id=user.id)
        return render(request,'home.html',{'c':c, 'i':i})
    else:
        return render(request,'home.html') 
    

@login_required(login_url='home')
def adminhome(request):
    return render(request,'adminhome.html')

# userhome
@login_required(login_url='home')
def userhome(request):
    c=Category.objects.all()
    return render(request,'userhome.html',{'c':c})

# login view
def loginn(request):
    c=Category.objects.all()
    return render(request,'login.html',{'c':c})

# login function
def login1(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pas = request.POST['password']
        usr = auth.authenticate(username=uname,password=pas) 
        if usr is not None:
            if usr.is_superuser:
                login(request,usr)
                return redirect('adminhome')
            else:
                c=Category.objects.all()
                i=Customer.objects.get(user_id=usr.id)
                login(request,usr)
                return render(request,'userhome.html',{'i':i,'c':c}) 

# logout
@login_required(login_url='home')
def logoutt(request):
    logout(request)
    return redirect('home') 

# user account create view
def signup(request):
    c=Category.objects.all()
    return render(request,'signup.html',{'c':c})

# user account create function
def signupaction(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pas = request.POST['pass']
        cpas = request.POST['cpass']
        email = request.POST['email']
        addrss = request.POST['address']
        contact = request.POST['contact']
        photo = request.FILES['image'] 

        if pas == cpas :
            if User.objects.filter(username = uname).exists():
                return redirect('signup')
            else:
                usr = User.objects.create_user(first_name = fname, last_name = lname, password = pas,email=email,username=uname) 
                usr.save()
                b = Customer(address = addrss,contactnumber=contact,image=photo,user=usr)
                b.save()
                return redirect('loginn')
        else:
            
            return redirect('signup')

# add category view
@login_required(login_url='home')
def add_category(request):
    return render(request,'add_category.html')

# add category fun
@login_required(login_url='home')
def addc(request):
    if request.method == 'POST':
        category = request.POST['category']
        c = Category(category=category)
        c.save()
        return redirect('add_category')

# add product view
@login_required(login_url='home')
def add_product(request):
    c=Category.objects.all()
    return render(request,'add_product.html',{'c':c}) 

# add product function
@login_required(login_url='home')
def addp(request):
    if request.method=='POST':
        prod = request.POST['pname']
        des = request.POST['des']
        cat = request.POST['category']
        price = request.POST['price'] 
        photo = request.FILES['photo']
        p = Product(productname=prod,description=des,price=price,image=photo,category_id=cat)
        p.save()
        return redirect('add_product')

# product details
@login_required(login_url='home')
def show_product(request):
    t = Product.objects.all()
    return render(request,'show_product.html',{'shw':t})

# user details
@login_required(login_url='home')
def show_user(request):
    s=Customer.objects.all()
    return render(request,'show_user.html',{'s':s}) 

# for diff category 
@login_required(login_url='home')
def filtr(request,pk):
    user=request.user
    i=Customer.objects.get(user_id=user.id)
    c=Category.objects.all()
    prd=Product.objects.filter(category=pk)
    return render(request,'filtr.html',{'c':c,'prd':prd,'i':i})

# add to cart function

@login_required(login_url='home')
def cart(request):
    c = Category.objects.all()
    use = request.user.id
    q = Customer.objects.get(user=use)
    b =q.id
    f = Cart.objects.filter(user_id=b)
    user=request.user
    i=Customer.objects.get(user_id=user.id)
    return render(request,'cart.html',{'c':c,'f':f,'i':i})

@login_required(login_url='home')
def addtocart(request,pk):
    cus = Customer.objects.get(user=request.user)
    n = cus.id
    p = Product.objects.get(id=pk)
    q = p.id
    m = Cart(product_id=q,user_id=n) 
    m.save()
    return redirect('cart')


# remove item from cart
@login_required(login_url='home')
def remove1(request,pk):
    r=Cart.objects.get(id=pk)
    r.delete()
    return redirect('cart')

# delete product
@login_required(login_url='home')
def deletep(request,pk):
    d=Product.objects.get(id=pk)
    d.delete()
    return redirect('show_product')

# delete user
@login_required(login_url='home')
def deleteu(request,pk):
    c=Customer.objects.get(user_id=pk)
    d=c.user.id 
    u=User.objects.get(id=d)
    c.delete() 
    u.delete()
    return redirect('show_user')