from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2307275903',
        'name': 'Rayhan Syahdira Putra',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
