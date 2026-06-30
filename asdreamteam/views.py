from django.shortcuts import render
from django.db.models import Count

from django.contrib.auth.models import User
from django.http import HttpResponse

# from news.models import News
# from gallery.models import Album, Photo

# Create your views here.


def home(request):
    
    template_name = 'home/index.html'
    page = 'home'
    
    # latest_news = News.objects.filter(is_active=True).order_by('-created_at')[:4]
    # albums = Album.objects.annotate(photo_count=Count('photos')).order_by('-created_at')[:4]
    
    context = {
        # 'latest_news'  : latest_news,
        # 'albums'       : albums,
        'page'         : page,
    }
    
    return render(request, template_name, context)  




def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "k.keita@asdreamteam.club", "#AsDTAdmn26")
        return HttpResponse("Admin created")
    return HttpResponse("Admin already exists")