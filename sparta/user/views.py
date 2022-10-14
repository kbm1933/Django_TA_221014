from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up_view(request):
    if request.method == 'GET':
        user  = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')

        if password != password2:
            return render(request, 'user/signup.html', {'error': 'Check Password!'})
        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html',{'error': 'user name and password check'})
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html',{'error':'This user Exist'})
            else:
                UserModel.objects.create_user(username=username, password=password,phone=phone,address = address)
                return redirect('/login')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        me = auth.authenticate(request,username=username,password=password) #로그인 정보 가져옴
        if me is not None:
            auth.login(request,me)
            return redirect('/')
        else:
            return render(request,'user/login.html',{'error':'유저이름 혹은 패스워드를 확인 해 주세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/login.html')