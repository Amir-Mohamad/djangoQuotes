from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path('', views.AllQuotes.as_view(template_name='api/allquotes.html'), name='allquotes'),
]
