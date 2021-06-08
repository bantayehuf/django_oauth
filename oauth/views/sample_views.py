from django.http import HttpResponse

def wecome(request):
    return HttpResponse("Welcome")