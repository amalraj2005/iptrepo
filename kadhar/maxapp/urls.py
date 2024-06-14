from django.urls import path
from .views import *
urlpatterns = [
    path('',AddTable.as_view(),name='add'),
    path('view',Viewtable.as_view(), name='loading'),
    path('edit/<int:id>',edittable.as_view(),name='edit'),
    path('delete/ <int:id>',deletetable.as_view(),name='delete')


]
