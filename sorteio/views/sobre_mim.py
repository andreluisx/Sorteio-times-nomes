from django.shortcuts import render

def sobre_mim(request):
    title = "Sobre o Dev"
    return render(request, 'sobre_mim.html', {'title': title})