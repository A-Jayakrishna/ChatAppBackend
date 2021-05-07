from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User,Message
from .serializers import UserSerializer,MessageSerializer
from django.contrib import messages

def validateUser(request):
    email=request.GET['email']
    pas=request.GET['pas'] 
    try:
        obj=User.objects.get(email=email)
        if obj.password==pas:
            return JsonResponse({'status':True,'id':obj.id,'name':obj.name})
        else:
            return JsonResponse({'status':"Wrong pass"})
    except:
        return JsonResponse({'status':"User not found"})

def userData(request):
    serialize=User.objects.all()
    data=UserSerializer(serialize,many=True)
    return JsonResponse(data.data,safe=False)

def msgData(request,convo):
    serialize=Message.objects.filter(convo=convo)
    data=MessageSerializer(serialize,many=True)
    return JsonResponse(data.data,safe=False)

def Insertrecord(request):
    serialize=User.objects.all()
    data = UserSerializer(serialize,many=True)
    d = data.data
    max_id = max(d2['id'] for d2 in d)
    name=request.GET['name']
    email=request.GET['email']
    password=request.GET['password']
    phone_no=request.GET['phone_no']

    obj = User(id=max_id+1,name=name,email=email,password=password,phone_no=phone_no)
    obj.save()
    messages.success(request,'Record Saved Successfull')
    return JsonResponse({'status':"passed"})