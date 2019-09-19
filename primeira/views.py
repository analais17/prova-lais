from django.shortcuts import render, redirect
from . models import Produto
from . forms import ProdutoForm
from . forms import PesquisaForm

def home (request):
     return render(request, 'home.html')

def produto_list (request):
    produtos=Produto.objects.all()     
    return render(request, 'list.html', {'produtos': produtos})

def produto_show(request, produto_id):
    produto=Produto.objects.get(pk=produto_id)
    return render(request, 'show.html', {'produto':produto})


def produto_form(request):
    if (request.method == 'POST'):
        form = ProdutoForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect ('/primeira/produtos/')    
        else:
            return render(request, 'form.html', {'form':form})  
       
    else:
        form = ProdutoForm()
        return render(request, 'form.html', {'form': form})      

def excluir_produto(request, produto_id):
     produto=Produto.objects.get(pk=produto_id)
     produto.delete()
     return redirect ('/primeira/produtos/')

def editar_produto (request, produto_id):
     if (request.method == 'POST'):
          produto=Produto.objects.get(pk=produto_id)
          form = ProdutoForm(request.POST, instance = produto)
          if form.is_valid():

              form.save()
              return redirect ('/primeira/produtos/')  
          else: 
              return render (request, 'editar.html', {'form':form, 'produto_id': produto_id})
    
     else:
         produto=Produto.objects.get(pk=produto_id)    
         form = ProdutoForm(instance = produto)
         return render (request, 'editar.html', {'form':form, 'produto_id': produto_id})

def pesquisa_form(request):
    if (request.method == 'POST'):
        form = PesquisaForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect ('/primeira/produtos/')    
        else:
            return render(request, 'list.html', {'form':form})  
       
    else:
        form = PesquisaForm()
        return render(request, 'list.html', {'form': form})   
#def pesquisa (request):
        
             


# Create your views here.
