from django.shortcuts import render,redirect
from .models import ProdectDetails

# Create your views here.

def addproduct(request):
    return render(request,'addproduct.html')

def add_product_details(request):
    if request.method=='POST':
        pname=request.POST['product_name']
        des=request.POST['description']
        qty=request.POST['quantity']
        price=request.POST['price']
        # img=request.POST['image']

        product=ProdectDetails(product_name=pname,
                               description=des,
                               quantity=qty,
                               Price=price)
        product.save()
        print("hii")
        return redirect('show_products')

def show_products(request):
    products=ProdectDetails.objects.all()
    return render(request,'prodectdetails.html',{'products':products})

def editpage(request,pk):
    products=ProdectDetails.objects.get(id=pk)
    return render(request,'edit.html',{'products':products})


def edit_product_details(request,pk):
    if request.method=='POST':
        products = ProdectDetails.objects.get(id=pk)
        products.product_name = request.POST.get('product_name')
        products.description = request.POST.get('description')
        products.quantity = request.POST.get('quantity')
        products.Price = request.POST.get('price')
        # products.image = request.FILES['image']
        products.save()
        return redirect('show_products')
    return render(request, 'edit.html',)

def deletepage(request,pk):
    products=ProdectDetails.objects.get(id=pk)
    return render(request,'delete.html',{'products':products})

#Deleting Product Element..
def delete_product(request,pk):
    products=ProdectDetails.objects.get(id=pk)
    products.delete()
    return redirect('show_products')

