from django.shortcuts import render

def mostrar_erro(request):
    erro = "Ocorreu um erro!"
    title = "Ocorreu um erro!"
    return render(request, 'erro.html', [{'erro': erro}, {'title': title}])
