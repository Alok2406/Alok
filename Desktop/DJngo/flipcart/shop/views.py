import json
from operator import le
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import OrdersUpdate, Product,Contact,Orders
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from .PayTm import Checksum
MERCHANT_KEY='h@F20He6@j6Vewws';

def index(request):
    # nSlides=n//4+ceil((n//4)-(n//4))
    allprods=[]
    catprods=Product.objects.values('catogory','id')
    cats = {item['catogory'] for item in catprods}
    for cat in cats :
        prod= Product.objects.filter(catogory=cat)
        n=len(prod)
        nSlides=n//4+ceil((n//4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])
    
    params={'allprods':allprods}
    return render( request,'shop/index.html' ,params)



def searchMatch(query,item):
    #return true if search is found else it returns false
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.catogory.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allprods=[]
    catprods=Product.objects.values('catogory','id')
    cats = {item['catogory'] for item in catprods}
    for cat in cats :
        prodtemp= Product.objects.filter(catogory=cat)
        prod= [item for item in prodtemp if searchMatch(query,item)]
        
        n=len(prod)
        nSlides=n//4+ceil((n//4)-(n//4))
        if len(prod)!=0:
                allprods.append([prod,range(1,nSlides),nSlides])
    
    params={'allprods':allprods, "msg": ""}
    if len(allprods) == 0 or len(query)<4 :
        params = {'msg': "Please make sure to Enter Valid Details"}
    return render( request,'shop/search.html' ,params)
    


def about(request):
    return render( request,'shop/about.html')


def contact(request):
    thank=False
    if request.method=="POST":
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        phone= request.POST.get('phone', '')
        desc= request.POST.get('desc', '')
        contact=Contact(name=name,phone=phone,email=email,desc=desc)
        contact.save()
        thank=True
    return render( request,'shop/contact.html', {'thank':thank})


def tracker(request):
    if request.method=="POST":
        orderId= request.POST.get('orderId', '')
        email= request.POST.get('email', '')
        
        try:
            order=Orders.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=OrdersUpdate.objects.filter(order_id=orderId)
                updates=[]
                
                for item in update:
                    updates.append({'text':item.update_desc,'time': item.timestamp})
                    response=json.dumps( {"status":"success","updates":updates,"itemsJson":order[0].items_json},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"NoItems"}')        
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request,'shop/tracker.html')


def productView(request, myid):
    #fetch the product using id
    product = Product.objects.filter(id=myid)
    print(product)
    return render( request,'shop/productview.html', {'product':product[0]})


def order(request):
    return render( request,'shop/Orders.html')


def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson',"")
        name= request.POST.get('name', '')
        amount= request.POST.get('amount', '')
        email= request.POST.get('email', '')
        address=request.POST.get('address1', '') + "" +request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code= request.POST.get('zip_code', '')
        phone= request.POST.get('phone', '')        
        
        order=Orders(items_json=items_json,name=name,amount=amount,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,)
        order.save()
        update= OrdersUpdate(order_id=order.order_id,update_desc="Your Order Has Been Placed")
        update.save()
        thank=True
        id=order.order_id
        #return render( request,'shop/checkout.html',{'thank':thank, 'id': id})
        param_dict={
            
            'MID': 'ZKuRjn82328068931632',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict['CHECKSUMHASH']= Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request,'shop/paytm.html',{'param_dict':param_dict})
        
    return render( request,'shop/checkout.html')    



@csrf_exempt
def handlerequest(request):
   
    form=request.POST
    response_dict={}
    for i in form.keys():
        response_dict[i]=form[i]
        if i =='CHECKSUMHASH':
            checksum = form[i]

    verify= Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order succesfully placed')

        else:
            print('order was unsuccesful' + response_dict['RESPMSG'])

    return render(request,'shop/paymentstatus.html',{'response':response_dict})
    # return HttpResponse('done')
    #paytm send post request here
