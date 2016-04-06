from django.shortcuts import render, redirect
from collection.forms import QuoteForm

from django.contrib.auth.decorators import login_required
from django.http import Http404

from collection.models import Quote
from django.template.defaultfilters import slugify

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    # This is a new view for the 'home' route defined in
    # urls.py of the project folder, next to settings.py
    return render(request, 'index.html', {
        'quotes': quotes,
    })

def create_quote(request):
    form_class = QuoteForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.slug = slugify(quote.author)
            quote.save()
            return redirect('quote_detail', slug=quote.slug)
    else:
        form = form_class()

    return render(request, 'create_quote.html', { 'form': form })


def quote_detail(request, slug):
    quote = Quote.objects.get(slug=slug)
    return render(request, 'quote_detail.html', {
        'quote': quote,
    })

@login_required
def edit_quote(request, slug):
    quote = Quote.objects.get(slug=slug)
    form_class = QuoteForm

    if quote.user != request.user:
        raise Http404
        
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('quote_detail', slug=quote.slug)
    else:
        form = form_class(instance=quote)

    return render(request, 'edit_quote.html', {
        'quote': quote,
        'form': form,
    })
