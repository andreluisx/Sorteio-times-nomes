from django.shortcuts import render

def pagina_inicial(request):
    title = "Ranked Custom"
    return render(request, 'pagina_inicial.html', {'title': title})