from django.shortcuts import render

# Create your views here.

def index(request):

    datas = {

    }
    return render(request, "pages/index.html", datas)

def about(request):

    datas = {

    }
    return render(request, "pages/about.html", datas)


def blog(request):

    datas = {

    }
    return render(request, "pages/blog.html", datas)

def services(request):

    datas = {

    }
    return render(request, "pages/services.html", datas)

def gallery(request):

    datas = {

    }
    return render(request, "pages/gallery.html", datas)

def contact(request):

    datas = {

    }
    return render(request, "pages/contact.html", datas)

def single(request):

    datas = {

    }
    return render(request, "pages/blog-single.html", datas)

