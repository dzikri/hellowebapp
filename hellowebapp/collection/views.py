from django.shortcuts import render

# Create your views here.
def index(request):
    number = 9
    # This is a new view for the 'home' route defined in
    # urls.py of the project folder, next to settings.py
    return render(request, 'index.html', { 'number': number })
