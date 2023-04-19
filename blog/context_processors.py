from .models import Category

def menu_links(request):
    links = Category.objects.filter(status=1).order_by('created_on')
    return dict(links=links)