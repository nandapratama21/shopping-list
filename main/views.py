from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Nanda Pratama',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
