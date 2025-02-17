# C:\Users\Admin\Desktop\skyhigh\brand\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('area/', views.brand_area, name='brand_area'),  # For homepage
    path('list/', views.brand_list, name='brand_list'),  # For dedicated brand list page
    path('<int:brand_id>/', views.brand_detail, name='brand_detail'),  # For brand detail page
]