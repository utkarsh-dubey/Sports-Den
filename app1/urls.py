from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.conf.urls import url, include
from .views import( posts_detail_view,
    posts_list_view, posts_create_view, basketball_view, pubg_view,
    cod_view, cricket_view)


urlpatterns = [
    path('',views.index,name="home"),

    path('signup',views.sign_up, name="sign_up"),
    path('posts2', views.home_view, name='posts'),
	url(r'^login/$',views.login_view,name="login"),
	url(r'^posts/$', posts_list_view, name='posts_list_view'),
    url(r'^posts/(?P<url>\S+)/$', posts_detail_view, name='posts_detail_view'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile, name='get_user_profile'),
    url(r'^create/$', posts_create_view, name='posts_create_view'),
    path('basketball', basketball_view, name='basketball'),
    path('pubg', pubg_view, name='pubg'),
    path('callofduty', cod_view, name='cod'),
    path('cricket', cricket_view, name='cricket'),
    path('football', views.football_view, name='football'),
    path('fifa', views.fifa_view, name='fifa'),
    path('fortnite', views.fortnite_view, name='fortnite'),
    path('ludo', views.ludo_view, name='ludo'),
    path('nba', views.nba_view, name='nba'),
    path('skribbl', views.skribbl_view, name='skribbl'),
    path('uno', views.uno_view, name='uno'),
    path('others', views.others_view, name='others'),
    path('chat', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room')
]
