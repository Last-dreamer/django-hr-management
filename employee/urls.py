from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    path('add', views.emp, name="add"),
    path('showemp', views.showemp, name="showemp"),
    path('updateEmp/<str:name>', views.updateEmp, name="updateEmp"),
    path('editemp/<str:name>', views.editemp, name="editemp"),
    path('deleteEmp/<str:name>', views.deleteEmp),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # inbuild login url
    path('/', include('django.contrib.auth.urls')),
]
