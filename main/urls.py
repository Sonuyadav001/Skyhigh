#C:\Users\Admin\Desktop\skyhigh\main\urls.py


# main/urls.py
from django.urls import path
from . import views
from .views import brochure_list

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about_area/', views.about_area_view, name='about_area'),

 
    path('gallery/', views.gallery_view, name='gallery'),
    path('portfolio/', views.portfolio_view, name='portfolio'),

    path("contact/", views.contact_view, name="contact"),
    
    path('blog_details', views.blog_details_view, name='blog_details'),
    path('about/', views.about_view, name='about'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),






   
    path('skincare/', views.skincare_view, name='skincare'),
    path('haircare/', views.haircare_view, name='haircare'),
    path('bodycare/', views.bodycare_view, name='bodycare'),

    path('babyandsensitiveskin/', views.baby_sensitive_skin_view, name='babyandsensitiveskin'),
  
    path('personalcare/', views.personalcare_view, name='personalcare'),
    

    path('custom-formulation-services/', views.custom_formulation_services_view, name='custom-formulation-services'),
    
    path('packaging-solutions/', views.packaging_solutions_view, name='packaging-solutions'),
    path('regulatory-legal-services/', views.regulatory_legal_services_view, name='regulatory-legal-services'),
    path('after-sales-support/', views.after_sales_support_view, name='after-sales-support'),


    path('faq/', views.faq_view, name='faq'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms_view, name='terms'),

    path('services/', views.service_list, name='service_list'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),

    path('brochures/', brochure_list, name='brochure_list'),

]
    #path('news/', views.news_view, name='news'),

"""
    path('services/', views.services_view, name='services'),
    path('services/detail/', views.services_detail_view, name='services_detail'),
    path('skincare/', views.skincare_view, name='skincare'),
    path('haircare/', views.haircare_view, name='haircare'),
    path('bodycare/', views.bodycare_view, name='bodycare_view'),




     path('services/', views.services_view, name='services'),
    path('services/<str:service_name>/', views.services_detail_view, name='services_detail'),
"""