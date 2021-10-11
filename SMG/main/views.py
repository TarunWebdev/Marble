from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def thecompany(request):
    return render(request,'thecompany.html')

