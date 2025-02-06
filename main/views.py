#C:\Users\Admin\Desktop\skyhigh\main\views.py
from django.shortcuts import render
from brand.models import Brand
from blog.models import Post
from django.http import JsonResponse
from .models import NewsletterSubscription
from .models import FAQ
from .models import Privacy
from .models import Term

def home_view(request):
    brands = Brand.objects.all()
    recent_posts = Post.objects.order_by('-date_posted')[:3]  # Fetch 3 most recent posts
    return render(request, 'main/home.html', {'brands': brands, 'recent_posts': recent_posts})
 
    
def about_area_view(request):
    return render(request, 'main/about_area.html')

def gallery_view(request):
    return render(request, 'main/gallery.html')

def portfolio_view(request):
    return render(request, 'main/portfolio.html')

def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'main/faq.html', {'faqs': faqs})

def privacy_view(request):
    privacys = Privacy.objects.all()
    return render(request, 'main/privacy.html', {'privacys': privacys})

    
def terms_view(request):
    terms = Term.objects.all()
    return render(request, 'main/terms.html', {'terms': terms})

"""
def news_view(request):
    return render(request, 'main/news.html')
"""

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        first_name = request.POST.get("firstn")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Save the message to the database
        ContactMessage.objects.create(
            first_name=first_name,
            email=email,
            phone=phone,
            message=message,
        )

        # Send email to admin
        try:
            send_mail(
                subject=f"New Contact Message from {first_name}",
                message=f"First Name: {first_name}\n\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}",
                from_email='sonubabua01@gmail.com',  # Replace with your email
                recipient_list=['sonutions1@gmail.com'],  # Admin email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send message: {e}")

        return redirect("contact")

    return render(request, "main/contact.html")




def blog_details_view(request):
    return render(request, 'page/blog-details.html')  



# views.py
def about_view(request):
    context = {
        'is_about_page': True,  # Add this context variable
    }
    return render(request, 'main/about.html', context)



# views.py
from django.shortcuts import render, get_object_or_404
from .models import Service, SubService

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service.html', {'services': services})

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Service, Brochure  # Import Brochure model

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    all_services = Service.objects.all()  # Pass all services for the sidebar
    brochures = Brochure.objects.all()  # Fetch all brochures

    return render(request, 'services/servicedetails.html', {
        'service': service,
        'all_services': all_services,
        'brochures': brochures,  # Pass brochures to the template
    })




"""
from django.shortcuts import render
from django.http import Http404

def services_detail_view(request, service_name):
    # Map valid service names to their template filenames
    valid_services = {
        'skincare': 'main/services/detail/skincare.html',
        'haircare': 'main/services/detail/haircare.html',
        'bodycare': 'main/services/detail/bodycare.html',
        'babyandsensitiveskin': 'main/services/detail/babyandsensitiveskin.html',

        'personalcare': 'main/services/detail/personalcare.html',
        
        'custom-formulation-services': 'main/services/detail/custom-formulation-services.html',
        
        'packaging-solutions': 'main/services/detail/packaging-solutions.html',

        'regulatory-legal-services': 'main/services/detail/regulatory-legal-services.html',

        'after-sales-support': 'main/services/detail/after-sales-support.html',
        # Add other services here
    }

    # Get the corresponding template for the service name
    detail_template = valid_services.get(service_name.lower())
    if not detail_template:
        raise Http404("Service not found")

    # Render the main service_detail.html and pass the detail template and service name
    return render(request, 'main/services/service_detail.html', {
        'detail_template': detail_template,
        'current_service': service_name.lower(),  # Pass the current service name
    })



"""




def services_view(request):
    return render(request, 'main/services/services.html')



def skincare_view(request):
    return render(request, 'main/detail/skincare.html')

def haircare_view(request):
    return render(request, 'main/detail/haircare.html')


def skincare_view(request):
    return render(request, 'main/detail/skincare.html')

def bodycare_view(request):
    return render(request, 'main/detail/bodycare.html')

def baby_sensitive_skin_view(request): 
    return render(request, 'main/detail/babyandsensitiveskin.html')

def personalcare_view(request):
    return render(request, 'main/detail/personalcare.html')

def custom_formulation_services_view(request):
    return render(request, 'main/detail/custom-formulation-services.html')

def packaging_solutions_view(request):
    return render(request, 'main/detail/packaging-solutions.html')

def regulatory_legal_services_view(request):
    return render(request, 'main/detail/regulatory-legal-services.html')

def after_sales_support_view(request):
    return render(request, 'main/detail/after-sales-support.html')






def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            return JsonResponse({'success': False, 'message': 'Email is required.'}, status=400)

        # Check if email already exists
        if NewsletterSubscription.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'You are already subscribed.'}, status=400)

        # Save the email
        NewsletterSubscription.objects.create(email=email)
        return JsonResponse({'success': True, 'message': 'Thank you for subscribing!'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


from django.shortcuts import render
from .models import Brochure

def brochure_list(request):
    brochures = Brochure.objects.all()
    return render(request, 'brochures.html', {'brochures': brochures})
