import random
from sorteio.forms import SorteioNomeForm
from django.shortcuts import render, redirect

def sorteio_nome(request):
    if request.method == 'POST':
        form = SorteioNomeForm(request.POST)
        if form.is_valid():
            nomes = form.cleaned_data['nomes']
            quantidade_vencedores = form.cleaned_data['quantidade_vencedores']
            nome_sorteio = form.cleaned_data['nome_sorteio']
            #divide os nomes
            participantes_sem_tratar = nomes.split('\n')
            # Embaralha as linhas
            random.shuffle(participantes_sem_tratar)
            participantes = []
            

           #tirando todo valor nulo da lista
            participantes = [nome for nome in participantes_sem_tratar if nome.strip()]

            #salvando os nomes pra usar na view resultado
            request.session['participantes'] = participantes
            request.session['quantidade_vencedores'] = quantidade_vencedores
            request.session['nome_sorteio'] = nome_sorteio
            

            #envia o usuário para a tela de resultado
            return redirect('sorteio:resultado_nome')
        
    else:
        form = SorteioNomeForm() 

    title = "Sorteio - Nomes"
    return render(request, 'sorteio_nome/index.html', {'title':title})
