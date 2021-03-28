from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'form.html')

def submit_page(request):
    if request.method == "POST":
        print(request.method)
        context = {
            'name': request.POST['name'],
            'lang': request.POST['fav_lang'],
            'location': request.POST['dojo_location'],
            'comment': request.POST['comment']
        }
        return render(request, 'submit_page.html', context)
    return render(request, 'submit_page.html')