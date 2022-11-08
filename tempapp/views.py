from django.shortcuts import render

# Create your views here.
def sport(request):
    return render(request,"testapp/sport.html")

def movie(request):
    return render(request,"testapp/movie.html")

def politics(request):
    return render(request,"testapp/politics.html")

def home(request):
    return render(request,"testapp/home.html")
