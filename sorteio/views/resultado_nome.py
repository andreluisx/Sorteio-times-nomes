from django.shortcuts import render

def resultado_nome(request):

    participantes = request.session.get('participantes')
    quantidade_vencedores = request.session.get('quantidade_vencedores')
    nome_sorteio = request.session.get('nome_sorteio')
    
    emoji = ['🥇', '🥈', '🥉', '🌹']
    
    quantiade_participantes = len(participantes)
    qntd_vencedores = int(quantidade_vencedores)

    vencedores = [participantes[i] + emoji[i] for i in range(qntd_vencedores)]

    contexto = {
        'quantiade_participantes': quantiade_participantes,
        'vencedores': vencedores,
        'nome_sorteio': nome_sorteio,
        'emoji': emoji
    }

    return render(request, 'sorteio_nome/resultado.html', contexto)