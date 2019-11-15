from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='index'),
    path('cv/', views.cv, name='cv'),
    path('blogs/', views.blog, name='blogs'),
    path('blogs/<category>/', views.blog_category, name='blog_category'),
    path("blogs/<category>/<int:blog_id>/", views.blog_detail, name="blog_detail"),
    path('photos/', views.photo, name='photos'),
    path('photos/<year>/', views.photo_folder, name='photo_folder'),
    path('calligraphy/', views.calligraphy, name='calligraphy'),
    path('calligraphy/<category>/', views.calligraphy_category, name='calligraphy_category'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)