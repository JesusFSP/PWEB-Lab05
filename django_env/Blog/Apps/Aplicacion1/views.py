from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'Apps.Aplicacion1/post_list.html', {})
