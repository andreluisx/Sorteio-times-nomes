import random
from sorteio.forms import SorteioForm
from django.shortcuts import render, redirect
from .functions import emojis

def sorteio_time(request):
    if request.method == 'POST':
        form = SorteioForm(request.POST)
        if form.is_valid():
            nomes = form.cleaned_data['nomes']
            quantidade_times = form.cleaned_data['quantidade_times']
            nome_sorteio = form.cleaned_data['nome_sorteio']
            #divide os nomes
            jogadores_sem_tratar = nomes.split('\n')
            # Embaralhar as linhas
            random.shuffle(jogadores_sem_tratar)
            jogadores = []
           
           #tirando todo valor nulo da lista
            jogadores = [jogador for jogador in jogadores_sem_tratar if jogador.strip()]

            #salvando os nomes pra usar na view resultado
            request.session['jogadores'] = jogadores
            request.session['quantidade_times'] = quantidade_times
            request.session['nome_sorteio'] = nome_sorteio
            request.session['emoji'] = emojis.emoji()

            #envia o usuário para a tela de resultado
            return redirect('sorteio:resultado_time')
        
    else:
        form = SorteioForm() 

    title = "Sorteio - Times"
    return render(request, 'sorteio_time/index.html', {'title':title})
