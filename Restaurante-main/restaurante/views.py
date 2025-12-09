from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from apps.mesas.models import Orden
from datetime import datetime
from datetime import timedelta
from django.db import models

def main_index(request):
  		return render(request, 'main/index.html')

@login_required(login_url='accounts:login')
def index_user(request):
    ordenes_hoy = Orden.objects.filter(estatus='pagada', fecha_hora__date=datetime.today())    
    total_sales = sum(orden.total for orden in ordenes_hoy)
    cantidad_ordenes = ordenes_hoy.count()
    ordenes_semana = Orden.objects.filter( estatus='pagada', fecha_hora__week=datetime.today().isocalendar()[1])

    # dias de la semana del 1 (lunes) al 7 (domingo)
    dias_semana = [datetime.today() - timedelta(days=datetime.today().isocalendar()[2] - 1) + timedelta(days=i) for i in range(7)]
    ventas_por_dia = []
    for dia in dias_semana:        
        ventas_dia = ordenes_semana.filter(fecha_hora__date=dia.date()).aggregate(total=Sum(models.F('detalles__cantidad') * models.F('detalles__precio_unitario')))['total'] or 0
        ventas_por_dia.append({'dia': dia.strftime('%Y-%m-%d'), 'total': ventas_dia})

    print(ventas_por_dia)
    
    # Ultimas 5 ordenes
    ultimas_ordenes = Orden.objects.all().order_by('-fecha_hora')[:5]
    
    #Platillos mas vendidos
    platillos_mas_vendidas = Orden.objects.filter(estatus='pagada').values('detalles__platillo__nombre').annotate(total_vendido=Sum('detalles__cantidad')).order_by('-total_vendido')[:10]

    context = {
        'ventas_totales': total_sales,
        'cantidad_ordenes': cantidad_ordenes,
        'ordenes_semana': ordenes_semana,
        'ventas_por_dia': ventas_por_dia,
        'ultimas_ordenes': ultimas_ordenes,
        'platillos_mas_vendidas': platillos_mas_vendidas,
    }
    
    return render(request, 'main/main_index.html', context)


