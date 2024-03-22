from django import forms

class SorteioForm(forms.Form):
    nomes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Use '*' para definir um líder..."}))
    quantidade_times = forms.ChoiceField(choices=[(2, '2 times'), (3, '3 times'), (4, '4 times'), (5, '5 times')])
    nome_sorteio = forms.CharField()

class SorteioNomeForm(forms.Form):
    nomes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Use '*' para definir um líder..."}))
    quantidade_vencedores = forms.ChoiceField(choices=[(1, '1 pessoa'), (2, '2 pessoas'), (3, '3 pessoas'), (4, '4 pessoas')])
    nome_sorteio = forms.CharField()
