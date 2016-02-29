from django.shortcuts import render
from collection.models import Quote

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    # This is a new view for the 'home' route defined in
    # urls.py of the project folder, next to settings.py
    return render(request, 'index.html', {
        'quotes': quotes,
    })

def quote_detail(request, slug):
    quote = Quote.objects.get(slug=slug)
    return render(request, 'quote_detail.html', {
        'quote': quote,
    })
