# C:\Users\Admin\Desktop\skyhigh\brand\views.py
from django.shortcuts import render, get_object_or_404
from .models import Brand

# View for brand_area.html (used on the homepage)
def brand_area(request):
    brands = Brand.objects.all()  # Retrieve all brands
    return render(request, 'brand/brand_area.html', {'brands': brands})

# View for brand_list.html (dedicated brand list page)
def brand_list(request):
    brands = Brand.objects.all()  # Retrieve all brands
    return render(request, 'brand/brand_list.html', {'brands': brands})

# View for brand_detail.html (brand detail page)
from django.shortcuts import render, get_object_or_404
from .models import Brand
from main.models import Brochure  # Ensure Brochure model is imported

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    gallery_images = brand.gallery.all()  # Fetch associated gallery images
    all_brands = Brand.objects.all()  # Fetch all brands for sidebar
    brochures = Brochure.objects.all()  # Fetch all brochures (modify if brand-specific)

    return render(request, 'brand/brand_detail.html', {
        'brand': brand,
        'gallery_images': gallery_images,
        'all_brands': all_brands,
        'brochures': brochures,  # Pass brochures to the template
    })

