from django.urls import path

from contato.views import CriarContatoView

app_name = 'contato'

urlpatterns = [
    path(f'{app_name}/criar', CriarContatoView.as_view(), name='criar'),
]