from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from music.models import Album
from django.contrib.auth.models import  User

# Create your views here.
def index(request):
    if request.user.is_authenticated: 
        albums = Album.objects.filter(user=request.user)
        user=request.user
        context = {
            'albums': albums,
            'user': user
        }
        return render(request, 'homepage/index.html', context)
    else:
        return redirect('homepage:login')

def MyLogin(request):
    if request.user.is_authenticated: 
        return redirect('homepage:index')
    else:
        if request.method == 'POST':
            # Lấy username và password
            username = request.POST.get('username')
            password = request.POST.get('password')  
            # kiểm tra xem username và password có trong dữ liệu không
            user = authenticate(username=username, password=password)
            if user is not None: # Nếu tìm thấy user có username và password đã nhập
                if user.is_active: # Tài khoản có bị vô hiệu chưa - đã/ còn hiệu lực
                    login(request, user)
                    # trả về trang index
                    # Lấy tất cả album của user đã đăng nhập
                    return redirect('homepage:index')
                else:
                    return render(request, 'homepage/login.html', {'message':'Tài khoản đã bị vô hiệu hóa'})
            else:
                return render(request, 'homepage/login.html', {'message':'Tài khoản không tồn tại'})

        return render(request, 'homepage/login.html')


def MyLogout(request):
    # Nếu không có tài khoản nào thì không thực hiện hàm đăng xuất
    try:
        logout(request)
    except:
        pass
    # Nếu đăng xuất thành công => trả về trang đăng nhập - login
    # return render(request, 'homepage/login.html')
    return redirect('homepage:login')

def MyRegister(request):
    # Nếu đã đăng nhập --> index
    if request.user.is_authenticated:
        return redirect('homepage:index')
    else:
        if request.method == 'POST':    
            # Lấy username, pass1 và pass2
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            # Kiểm tra username, password1 và password2 có rỗng hoặc password1 != password2 hay không
            if username == '' or password1 == '' or password2 == '' or password1 != password2:
                return render(request, 'homepage/register.html')
            else:
                new_user = User()
                new_user.username = username
                new_user.set_password(password1)
                new_user.save()
                user = authenticate(username=username, password=password1)
                login(request, user)
                return redirect('homepage:index')

        return render(request, 'homepage/register.html')
