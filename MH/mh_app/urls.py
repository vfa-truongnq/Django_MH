from django.urls import path
from . import views

urlpatterns = [
    path('<id>/',views.api_detail_mh),
    path('<id>/update/',views.api_update_mh),
    path('<id>/delete/',views.api_delete_mh),
    path('create/',views.api_create_mh)
]