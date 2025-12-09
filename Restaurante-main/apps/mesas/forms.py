import django.forms as forms
from .models import MesasEstado, Mesa, Orden, OrdenDetalle, MetodoPago, Pago
from apps.platillos.models import Platillo

class MesasEstadoForm(forms.ModelForm):
    class Meta:
        model = MesasEstado
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del estado de la mesa'})
        }
        
class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['nombre', 'capacidad', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la mesa'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de la mesa'}),
            'estado': forms.Select(attrs={'class': 'form-control'})
        }
        
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['mesa', 'empleado']
        widgets = {
            'mesa': forms.Select(attrs={'class': 'form-control'}),
            'empleado': forms.HiddenInput(attrs={'class': 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if 'mesa' in self.fields:
                self.fields['mesa'].queryset = Mesa.objects.filter(estado__nombre__iexact='Disponible')
    
    def save(self, commit=True):
        orden = super().save(commit=False)
        if commit:
            orden.estatus = 'pendiente' 
            orden.empleado = self.initial['empleado']
            orden.save()
            mesa = orden.mesa
            mesa.estado = MesasEstado.objects.get(nombre='Ocupada')
            mesa.save()
        return orden
    
class OrdenDetalleForm(forms.Form):
    platillo = forms.ModelChoiceField(queryset=Platillo.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    notas = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=False)    
    orden_id = forms.IntegerField(widget=forms.HiddenInput())
    
class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del metodo de pago'})
        }
        
class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['orden', 'metodo_pago', 'cantidad']
        widgets = {
            'orden': forms.HiddenInput(),
            'metodo_pago': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'})
        }