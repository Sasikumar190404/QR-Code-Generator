from django.shortcuts import render,HttpResponse
from .models import QRCodeForm
import qrcode
import os
from django.conf import settings
# Create your views here.


def generate_qr_code(request):
    if request.method == 'POST':
        name=request.POST.get('restaurant_name')
        url=request.POST.get('menu_url')
    
        obj=QRCodeForm()
        obj.restaurant_name=name
        obj.url=url
        obj.save()
        
        qr=qrcode.make(obj.url)
        file_name=name.replace(" ","_").lower()+'_menu.png'
        file_path=os.path.join(settings.MEDIA_ROOT,file_name)
        qr.save(file_path) 
        
        qr_url = os.path.join(settings.MEDIA_URL,file_name)
        
        return render(request,'qr_result.html',{'name':name,"qr_url":qr_url,'file_name':file_name})
        
        
    return render(request,'generate_qr_code.html')