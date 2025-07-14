from django.shortcuts import render

def index_view(request):
    if request.method == "GET":
        return render(request, 'home.html')