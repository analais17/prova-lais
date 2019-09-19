from django.forms import ModelForm
from . models import Produto



class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

 
class PesquisaForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'        