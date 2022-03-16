from django.urls import path
from . import views

urlpatterns = [
    path('mh/create/',views.api_create_mh),
    path('mh/',views.api_get_list),
    path('getByRadius',views.api_get_list_radius),
    path('mh/<id>/',views.api_detail_mh),
    path('mh/<id>/delete/',views.api_delete_mh),
    path('mh/<id>/update/',views.api_update_mh),
    
]