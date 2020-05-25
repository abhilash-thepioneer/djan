from django.shortcuts import render
from django.http import HttpResponse
from .models import Productnew,Contact,Orders,OrderUpdate
from math import ceil
import json
from .PayTm import Checksum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


MERCHANT_KEY = 'kbzk1DSbJiV_03p5'
# Create your views here.
import logging
from django.views.decorators.csrf import csrf_exempt

#thank=False

logger=logging.getLogger(__name__)
def index(request):
	#products=Productnew.objects.all()
	#print(products)
	allProducts=[]
	catprods=Productnew.objects.values('category','id')
	#cats={item['category'] for item in catprods}
	cats={item['category'] for item in catprods}
	#allProducts=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
	for cat in cats:
		prod=Productnew.objects.filter(category=cat)
		n=len(prod)
		nSlides= (n//4)+ceil((n/4)-(n//4))
		allProducts.append([prod,range(1,nSlides),nSlides])
	params={'allProducts':allProducts}

	return render(request,'shop/index.html',params)

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Productnew.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Productnew.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)

def about(request):
	return render(request,'about.html')

def contact(request):
	#thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        cont = Contact(name=name, email=email, phone=phone, desc=desc)
        cont.save()
        thank= True
    return render(request, 'shop/contact.html')


@login_required(login_url='/account/login/')
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))

    return render(request, 'shop/tracker.html')


def productView(request,myid):
	product=Productnew.objects.filter(id=myid)
	print(product)
	return render(request,'shop/productView.html',{'product':product[0]})

@login_required(login_url='/account/login')
def checkout(request):
    if request.method=="POST" :
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # Request paytm to transfer the amount to your account after payment by user
       
        #param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        #return render(request, 'shop/paytm.html', {'param_dict': param_dict})

    return render(request, 'shop/checkout.html')

def tp(request):
	return render(request,'shop/timepass.html')
def items(request):
    if request.method=="POST":
        allProductss=[]
        catprods=Productnew.objects.values('category','id')
        #cats={item['category'] for item in catprods}
        cats={item['category'] for item in catprods}
        #allProducts=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
        for cat in cats:
            prod=Productnew.objects.filter(category=cat,seller=request.POST.get('userr'))
            n=len(prod)
            nSlides= (n//4)+ceil((n/4)-(n//4))
            if n>0:
                allProductss.append([prod,range(1,nSlides),nSlides])
    params={'allProducts':allProductss}

    return render(request,'shop/items.html',params)

@csrf_exempt
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    #checksum=''
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})