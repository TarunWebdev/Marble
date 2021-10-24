from django.shortcuts import render
from main.models import Blog , StoneType , Stone , CarouselCategory , CarouselImages

# Create your views here.
#Need modelS
def index(request):
    stones = StoneType.objects.all()
    carousel = CarouselCategory.objects.all()
    carouselCatFilter = 
    return render(request,'index.html',{'stones': stones})


#ABOUT SMG
def thecompany(request):
    return render(request,'thecompany.html')

def management(request):
    return render(request,'management-Shiv-Marble-and-Granite.html')

def capacity(request):
    return render(request,'production-capacity.html')


def stonecollection(request):
    stonesType = StoneType.objects.all()
    return render(request , 'products.html' , {'stonesType': stonesType})
    # sends all stone type

def stone(request):
    s_name = str(request.GET["StoneType"])
    stones = Stone.objects.select_related('StoneType').filter(category__name=s_name)
    stoneType = StoneType.objects.filter(chapter_name=s_name)
    return render(request, "singleStone.html", {'stones': stones, 'stoneType': stoneType})
    # sends stones of a particular category

# NEW FRONTEND
def blogs(request):
    blogs = Blog.objects.all()
    return render(request , 'blogs.html' , {'blogs': blogs})
    # sends all blogs for 'coming soon page'


def pageBlog(request):
    bObjget = str(request.GET["title"])
    blogs = Blog.objects.filter(title=bObjget)
    return render(request, "blogs.html", {'bObj': blogs})
# New blog Page from Github which will be for single Blog view


#STATIC
def contact(request):
    return render(request , 'contact.html')

def stonecraft(request):
    return render(request , 'stone-crafting-process.html')

def whysmg(request):
    return render(request , 'why-Shiv-Marble-and-Granite.html')

