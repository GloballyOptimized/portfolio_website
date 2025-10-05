from django.urls import path
from landing_page.views import landing_page

urlpatterns = [
    path('landing_page/', landing_page, name='landing_page'),
]
