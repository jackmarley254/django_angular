from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to my Library API</h2><p>Go to <a href='/api/books/'>/api/books/</a></p>")
