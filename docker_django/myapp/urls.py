from django.urls import path
from . import views
from .views import SearchCreatedTickets, SearchCompletedTickets

#
urlpatterns = [
    #URL GLOBALES
    path('', views.signin, name = 'singin'),
    path('main/', views.main, name = 'main'),
    path('logout/', views.signout, name = 'logout'),

    #URL TICKETS
    path('tickets/', views.tickets, name = 'tickets'),
    path('ticket/create', views.create_ticket, name = 'create_ticket' ),
    path('ticket/<int:ticket_id>/progress', views.progress_ticket, name = 'progress_ticket'),
    path('ticket/<int:ticket_id>/history', views.historial_ticket, name = 'historial_ticket'),
    path('ticket/<int:ticket_id>/add', views.add_registro_ticket, name = 'add_registro_ticket'),
    path('ticket/<ticket_id>/deactivate', views.deactivate_ticket, name = 'deactivate_ticket'),
    path('ticket/<int:ticket_id>/area', views.add_ticket_to_area, name = 'add_ticket_to_area'),
    path('ticket/<int:ticket_id>/<str:cod_area>/del', views.delete_ticket_to_area, name = 'delete_ticket_to_area'),

    path('tickets/report', views.report_tickets_view, name = 'report_tickets'),
    #path('tickets/completed', views.completed_tickets, name = 'completed_tickets'),

    #URL TESTING
    #path('tickets/export', views.export_csv, name = 'export_tickets_csv'),
    path('tickets/created', SearchCreatedTickets.as_view(), name='search_tickets'),
    path('tickets/completed', SearchCompletedTickets.as_view(), name = 'completed_tickets'),

    #UPLOAD URLS
    path('import/<str:model>', views.auto_import, name='import_model'),
    #path('users/import', views.users_import, name='import_users')

    #REPORT
    # path('report/tickets/pdf', views.report_all_tickets_pdf, name = 'report_tickets_pdf'),
    path('report/tickets/xls', views.report_all_tickets_xls, name = 'report_tickets_xls')
    ]