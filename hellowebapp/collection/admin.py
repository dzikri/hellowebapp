from django.contrib import admin

# Register your models here.
from collection.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ('author', 'text', 'description')
    prepopulated_fields = {'slug': ('author',)}

admin.site.register(Quote, QuoteAdmin)
