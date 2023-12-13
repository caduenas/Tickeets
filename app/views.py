from django.shortcuts import render

def post_list(request):
    return render(request, 'app/index.html', {})

# Create your views here.
