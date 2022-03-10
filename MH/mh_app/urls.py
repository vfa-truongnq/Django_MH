from django.urls import path
from . import views

urlpatterns = [
    path('mh/create/',views.api_create_mh),
    path('mh/list/',views.api_get_list),
    path('mh/<id>/',views.api_detail_mh),
    path('mh/<id>/update/',views.api_update_mh),
    path('mh/<id>/delete/',views.api_delete_mh)
]