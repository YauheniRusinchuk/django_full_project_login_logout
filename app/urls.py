from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, about, add_post, addpost, profile, post_detail, search
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('search/',search, name='search'),
    path('postnumber/<int:pk>/', post_detail, name='detail'),
    path('about/', about, name='about'),
    path('addpost/', addpost, name='addpost'),
    path('add/', add_post, name='add'),
    path('', index, name='index'),
    path('profile/<str:fullname>/', profile, name='profile'),
    path('login/', auth_views.login,  {'template_name': 'app/login.html'}),
    path('logout/', auth_views.logout, {"next_page" : "/"}, name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
