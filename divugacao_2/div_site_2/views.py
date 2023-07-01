from django.shortcuts import render, redirect, HttpResponse
#esta importando a class que contem a tabela dos produtos
from .models import produto
#importa o formulario do dajango
from .forms import produtoForm
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.http import FileResponse
#from fpdf import FPDF
from django.contrib.auth.decorators import login_required
from datetime import datetime




# Create your views here.

def home(request):
    return render(request, 'home/home.html')

@login_required
def cadastramento(request):
    #verifica se é novo cadatro ou atualizando
    if request.method == 'POST':
        produto_form = produtoForm(request.POST)
        # verifica se as informaçoes sao validas
        if produto_form.is_valid():
            produto_form.save()
        #redirecionamento
        return redirect ('tela')
    else:
        produto_form = produtoForm()
        formulario={
            'formulario':produto_form
        }
        return render(request, 'cadastramento/cadastro.html', context=formulario)
    
@login_required
def visualizacao(request):
    #cria um dicionario para pegar todos os dados
    dados = {
        # chave : tabela.pega_todos_objetos.exibir_todos_objetos()
        'dados' : produto.objects.all()
    }
    # chama o dicionario atraves do context=
    return render(request, 'visualizacao/tela.html', context=dados)

@login_required
def detalhe(request,id_produto):
    #basicamente cria um dicionario e pega as informaçoes com base na chave primaria
    dados = {
        'dados':produto.objects.get(pk=id_produto)
        }
    return render(request, 'detalhe/detalhes.html',dados)

@login_required
def editar(request,id_produto):
    produtos = produto.objects.get(pk=id_produto)
    if request.method == 'GET':
        formulario = produtoForm(instance=produtos)
        return render(request, 'cadastramento/cadastro.html',{'formulario': formulario})
    else:
        formulario = produtoForm(request.POST,instance=produtos)
        if formulario.is_valid():
            formulario.save()
        return redirect('tela')

@login_required   
def excluir(request, id_produto):
    produtos = produto.objects.get(pk=id_produto)
    if request.method == 'POST':
        produtos.delete()
        return redirect('tela')
    return render(request, 'delete/excluir.html',{'item': produtos})

@login_required
def filtro(request):
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    placa = request.GET.get('placa')

    produtos_filtrados = None
    if data_inicio and data_fim and placa:
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()

        produtos_filtrados = produto.objects.filter(data__range=(data_inicio, data_fim), placa=placa)

    # if request.GET.get('download') == 'true':
    #     # Cria um objeto BytesIO para armazenar o PDF em memória
    #     buffer = BytesIO()

    #     # Cria o objeto PDF usando o objeto BytesIO como saída
    #     p = canvas.Canvas(buffer, pagesize=letter)

    #     # Define as dimensões e estilos da página
    #     width, height = letter

    #     # Define as dimensões e estilos da tabela
    #     x_start = 30
    #     y_start = height - 100
    #     table_width = width - x_start * 2
    #     col_width = table_width / 8  # Aumente o número de colunas para 8
    #     row_height = 20

    #     # Reduza o tamanho interno da tabela
    #     table_width -= 100

    #     # Define o cabeçalho da tabela
    #     header = ['ID', 'Fornecedor', 'Data', 'Solicitante', 'Autorizado', 'Item', 'Placa', 'Valor']

    #     # Escreve o cabeçalho da tabela
    #     p.setFont("Helvetica-Bold", 10)
    #     p.setFont("Helvetica-Bold", 10)
    #     for i, header_item in enumerate(header):
    #         x = x_start + i * col_width + col_width / 2  # Calcula a posição centralizada
    #         p.drawCentredString(x, y_start, header_item)

    #     p.setFont("Helvetica", 8)
    #     if produtos_filtrados:
    #         y = y_start - row_height
    #         for i, item in enumerate(produtos_filtrados):
    #             x = x_start  # Define a posição inicial para cada linha de informações
    #             p.drawCentredString(x + col_width * 0.5, y, str(item.id))
    #             p.drawCentredString(x + col_width * 1.5, y, str(item.fornecedor))
    #             p.drawCentredString(x + col_width * 2.5, y, str(item.data))
    #             p.drawCentredString(x + col_width * 3.5, y, str(item.solicitante))
    #             p.drawCentredString(x + col_width * 4.5, y, str(item.autorizado))
    #             p.drawCentredString(x + col_width * 5.5, y, str(item.item))
    #             p.drawCentredString(x + col_width * 6.5, y, str(item.placa))
    #             p.drawCentredString(x + col_width * 7.5, y, str(item.valor))

    #             y -= row_height



        # else:
        #     p.drawString(x_start, y_start - row_height, "Nenhum dado encontrado.")

        # # Encerra o objeto PDF
        # p.showPage()
        # p.save()

        # # Move para o início do objeto BytesIO para leitura
        # buffer.seek(0)

        # # Cria a resposta HTTP com o conteúdo PDF
        # response = FileResponse(buffer, content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="dados.pdf"'

        # return response

    context = {'dados': produtos_filtrados}
    return render (request, 'detalhe/filtro.html', context)
