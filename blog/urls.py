from django.urls import path
from .views import home_page, gallery_page, about_page, gallery_detail, submit_comment

urlpatterns = [
    path('', home_page, name='home_page'),
    path('gallery/', gallery_page, name='gallery'),
    path('gallery/<int:pk>/', gallery_detail, name='gallery_detail'),
    path('about/', about_page, name='about'),
    path('submit_comment/<int:pk>/', submit_comment, name='submit_comment')
]
