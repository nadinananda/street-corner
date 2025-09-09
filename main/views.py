from django.shortcuts import render
from .models import Product

def show_main(request):

    context = {
        'nama aplikasi' : 'street corner',
        'npm' : '2406351806',
        'name': 'Nadin Ananda',
        'class': 'PBP E',
    }

    return render(request, "main.html", context)
