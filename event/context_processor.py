from .models import Category


def categories_processor(request):
    category_events = Category.objects.all()
    return {"categories": category_events}
