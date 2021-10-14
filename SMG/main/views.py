from django.shortcuts import render

# Create your views here.
#Need model
def index(request):
    return render(request,'index.html')


#ABOUT SMG
def thecompany(request):
    return render(request,'thecompany.html')

def management(request):
    return render(request,'management-Shiv-Marble-and-Granite.html')

def capacity(request):
    return render(request,'production-capacity.html')


#Need model
def stonecollection(request):
    return render(request , 'products.html')

# NEW FRONTEND
# def blogs(request):
#     return render(request , 'blogs.html')


#STATIC
def contact(request):
    return render(request , 'contact.html')

def stonecraft(request):
    return render(request , 'stone-crafting-process.html')

def whysmg(request):
    return render(request , 'why-Shiv-Marble-and-Granite.html')

