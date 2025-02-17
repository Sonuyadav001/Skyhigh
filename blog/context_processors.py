from .models import Tag

def tags_processor(request):
    """
    Adds all tags to the context, so they are available on every page.
    """
    return {'tags': Tag.objects.all()}
