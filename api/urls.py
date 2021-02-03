from django.urls import path
from . import views


urlpatterns = [
    path('', AllQuotes.as_view(template_name='api/allquotes.html'), name='allquotes'),
]
