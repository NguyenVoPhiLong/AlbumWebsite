from django.shortcuts import render, redirect
from music.models import *

# Create your views here.
def AddAlbum(request):
    # nếu chưa đăng nhập --> yêu cầu đăng nhập
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            star = request.POST.get('star')
            logo = request.POST.get('logo')
            if title == '' or star == '' or logo == '':
                return render(request, 'music/add_album.html')
            else:
                new_album = Album()
                new_album.title = title
                new_album.star = star
                new_album.logo = logo
                # lưu tên người tạo
                new_album.user = request.user
                new_album.save()
                return redirect('homepage:index')

        return render(request, 'music/add_album.html')
    else:
        return redirect('homepage:login')

def DeleteAlbum(request, id):
    # nếu chưa đăng nhập --> yêu cầu đăng nhập
    if request.user.is_authenticated:
        get_album = Album.objects.get(albumid=id)
        get_album.delete()
        # sau khi xoá trả về trang index
        return redirect('homepage:index')
    else:
        return redirect('homepage:login')

def EditAlbum(request, id):
    if request.user.is_authenticated:
        get_album = Album.objects.get(albumid=id)
        if request.method == 'POST':
            title = request.POST.get('title')
            star = request.POST.get('star')
            logo = request.POST.get('logo')

            # update album
            get_album.title = title
            get_album.star = star
            get_album.logo = logo
            get_album.save()

            # sau khi chỉnh sửa -> trả về trang index
            return redirect('homepage:index')

        context = {
            'album': get_album,
        }

        # vào trang chỉnh sửa
        return render(request, 'music/edit_album.html', context)
    else:
        return redirect('homepage:login')