from django.shortcuts import render
from django.contrib import messages

def resultado_time(request):
    #recebendo as variaveis da view sorteio
    jogadores = request.session.get('jogadores')
    numero_de_times = request.session.get('quantidade_times')
    nome_sorteio = request.session.get('nome_sorteio')
    emoji = request.session.get('emoji')


    qntd_jogadores = len(jogadores) #pegando a quantidade total de jogadores
    quantidade_times = int(numero_de_times) #alterando o tipo de char para int

    #dividindo os jadores por time e salvando nas variaveis times, caso seja possivel fazer a divisão
    try:
        jogador_por_time = qntd_jogadores // quantidade_times
        times = [jogadores[i:i+jogador_por_time] for i in range(0, len(jogadores), jogador_por_time)]
    except ZeroDivisionError and ValueError as e:
        erro = str(e)  
        return render(request, 'sorteio_time/index.html')
    
    
    title = "Sorteio - Resultado"

    #se times e quantidade_times não forem nulos vai renderizar o resultado.html e enviar variaveis no contexto
    if times and quantidade_times and nome_sorteio:
        contexto = {
            'times': times,
            'qntd_jogadores': qntd_jogadores,
            'quantidade_times': quantidade_times,
            'nome_sorteio': nome_sorteio,
            'title': title,
            'emoji': emoji,
        }
        return render(request, 'sorteio_time/resultado.html', contexto)
    
    else:
        messages.error(request, 'Os dados do sorteio não foram encontrados.')

    return render(request, 'sorteio_time/resultado.html')
