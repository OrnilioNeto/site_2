from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from django.forms import ModelForm
from .models import produto

class produtoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('item', css_class='campo-lado-a-lado', style='width: 200px;'),
                Field('placa', css_class='campo-lado-a-lado', style='width: 150px;'),
                Field('valor', css_class='campo-lado-a-lado', style='width: 100px;'),
                Field('fornecedor', css_class='campo-lado-a-lado', style='width: 250px;'),
                Field('data', css_class='campo-lado-a-lado', style='width: 120px;'),
                Field('solicitante', css_class='campo-lado-a-lado', style='width: 180px;'),
                Field('autorizado', css_class='campo-lado-a-lado', style='width: 80px;'),
                Field('nivel', css_class='campo-lado-a-lado', style='width: 50px;'),
                # Outros campos do formulário
                css_class='formulario_crispy'
            ),
        )


    class Meta:
        model = produto
        fields = '__all__'
