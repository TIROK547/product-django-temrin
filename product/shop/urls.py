from django.urls import path
from .views import info_response, terms_response, buy_response
urlpatterns = [
    path("info",info_response),
    path("terms",terms_response),
    path("buy/<int:quantity>",buy_response),
]
