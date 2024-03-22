from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def contar_linhas(request):
    if request.method == 'POST':
        texto = request.POST.get('texto', '')
        total_linhas = texto.count('\n') + 1
        return JsonResponse({'total_linhas': total_linhas})
    else:
        return JsonResponse({'error': 'Método inválido'})
