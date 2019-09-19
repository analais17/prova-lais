from django.db import models


class Carrinho_De_Compras (models.Model):
    capacidade=models.CharField(max_length=50)
    valor_carrinho = models.CharField(max_length=11)
  

class Produto (models.Model):
    nome = models.CharField(max_length=50)
    preco= models.CharField(max_length=11)
    quantidade=models.CharField(max_length=11)
    carrinho_de_compras=models.ForeignKey(Carrinho_De_Compras, on_delete=models.CASCADE) 
    def __str__(self):
        return self.produto
    
   

class Cliente (models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=11)
    cpf= models.CharField(max_length=10)
    carrinho_de_compras=models.ForeignKey(Carrinho_De_Compras,on_delete=models.CASCADE, primary_key=True)




    

# Create your models here.
