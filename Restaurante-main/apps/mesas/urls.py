from django.urls import path
from . import views

app_name = 'mesas'

urlpatterns = [  
    path('mesas_estado/', views.MesasEstadoListView.as_view(), name='mesas_estado_list'),
    path('mesas_estado/add/', views.MesasEstadoCreateView.as_view(), name='mesas_estado_create'),
    path('mesas_estado/<int:pk>/edit/', views.MesasEstadoUpdateView.as_view(), name='mesas_estado_edit'),
    path('mesas_estado/<int:pk>/delete/', views.MesasEstadoDeleteView.as_view(), name='mesas_estado_delete'),
      
    path('mesas/', views.MesaListView.as_view(), name='mesas_list'),
    path('mesas/add/', views.MesaCreateView.as_view(), name='mesas_create'),
    path('mesas/<int:pk>/edit/', views.MesaUpdateView.as_view(), name='mesas_edit'),
    path('mesas/<int:pk>/delete/', views.MesaDeleteView.as_view(), name='mesas_delete'),
    
    path('ordenes/', views.OrdenListView.as_view(), name='ordenes_list'),
    path('ordenes/add/', views.OrdenCreateView.as_view(), name='ordenes_create'),
    
    path('ordenes/<int:orden_id>/detalles/', views.OrdenDetalleView.as_view(), name='ordenes_detalle_list'),
    path('ordenes/<int:pk>/detalles/edit/', views.OrdenDetalleUpdateView.as_view(), name='ordenes_detalle_update'),
    path('ordenes/detalles/eliminar/<int:pk>/', views.OrdenDetalleDeleteView.as_view(), name='ordenes_detalle_delete'),
    
    path('ordenes/<int:orden_id>/pagar', views.OrdenPagarView.as_view(), name='ordenes_pagar'),
    
    path('metodos_pago/', views.MetodoPagoListView.as_view(), name='metodos_pago_list'),
    path('metodos_pago/add/', views.MetodoPagoCreateView.as_view(), name='metodos_pago_create'),
    path('metodos_pago/<int:pk>/edit/', views.MetodoPagoUpdateView.as_view(), name='metodos_pago_edit'),
    path('metodos_pago/<int:pk>/delete/', views.MetodoPagoDeleteView.as_view(), name='metodos_pago_delete'),
    
    path('pagos/', views.PagoListView.as_view(), name='pagos_list'),
]