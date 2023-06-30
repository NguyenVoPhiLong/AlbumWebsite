from django.urls import path
from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('login',  views.MyLogin, name="login"), # <- Tạo đường dẫn đến hàm login trong views.py ở hompage
    path('logout', views.MyLogout, name="logout"),
    path('register', views.MyRegister, name='register')
]