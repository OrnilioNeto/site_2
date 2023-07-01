from django.db import models
from datetime import datetime

# para criar novas migrations ; python manage.py makemigrations
# para atualizar as migrates para o BD : python manage.py migrate
# para rodar o servidor : python manage.py runserver
# para criar um app : python manage.py startapp cadastro
# para criar um projeto : django-admin startproject cadastro_servicos
#para crair usuario : python manage.pt creatsuperuser

# Create your models here.
class produto(models.Model):
    item = models.TextField(max_length=15)
    placa= models.TextField(max_length=7)
    valor =models.FloatField()
    fornecedor = models.TextField(max_length=15)
    data = models.DateField(default=datetime.now)
    solicitante = models.TextField(max_length=15)
    autorizado = models.BooleanField(default=False)
    nivel = models.IntegerField(default=1)




 