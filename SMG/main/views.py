from django.shortcuts import render
from main.models import Blog , StoneType , Stone , CarouselCategory , CarouselImages

# Create your views here.
#Need modelS
def index(request):
    stones = StoneType.objects.all()
    carousel = CarouselCategory.objects.all()
    carouselFilter = []
    for i in carousel :
        temp = i.name.replace(" ", "_").lower()
        carouselFilter.append(temp)
    mylist = zip(carousel, carouselFilter)
    carouselImages = CarouselImages.objects.all()
    carouselImagesFilter = []
    for i in carouselImages :
        temp = i.category.name.replace(" ", "_").lower()
        carouselImagesFilter.append(temp)
    mylist2 = zip(carouselImages, carouselImagesFilter)
    return render(request,'index.html',{'stones': stones ,'mylist':mylist , 'mylist2':mylist2})


#ABOUT SMG
def thecompany(request):
    stones = StoneType.objects.all()
    return render(request,'thecompany.html' , {'stones': stones})

def management(request):
    stones = StoneType.objects.all()
    return render(request,'management-Shiv-Marble-and-Granite.html' , {'stones': stones})

def capacity(request):
    stones = StoneType.objects.all()
    return render(request,'production-capacity.html' , {'stones': stones})


def stonecollection(request):
    stonesType = StoneType.objects.all()
    return render(request , 'products.html' , {'stonesType': stonesType})
    # sends all stone type

def stone(request):
    s_name = str(request.GET["StoneType"])
    stones = Stone.objects.select_related('category').filter(category__name=s_name)
    stoneType = StoneType.objects.filter(name=s_name)
    return render(request, "singleStone.html", {'stones': stones, 'stoneType': stoneType})
    # sends stones of a particular category

# NEW FRONTEND
def blogs(request):
    stones = StoneType.objects.all()
    blogs = Blog.objects.all()
    return render(request , 'blogs.html' , {'blogs': blogs ,'stones': stones})
    # sends all blogs for 'coming soon page'


def pageBlog(request):
    bObjget = str(request.GET["title"])
    blogs = Blog.objects.filter(title=bObjget)
    return render(request, "blog.html", {'bObj': blogs})
# New blog Page from Github which will be for single Blog view


#STATIC
def contact(request):
    stones = StoneType.objects.all()
    return render(request , 'contact.html' , {'stones': stones})

def stonecraft(request):
    stones = StoneType.objects.all()
    return render(request , 'stone-crafting-process.html' , {'stones': stones})

def whysmg(request):
    stones = StoneType.objects.all()
    return render(request , 'why-Shiv-Marble-and-Granite.html' , {'stones': stones})

