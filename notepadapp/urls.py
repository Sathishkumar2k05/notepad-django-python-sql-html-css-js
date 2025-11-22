from django.urls import path
from .views import *

urlpatterns=[
    path('',NotePadListView.as_view(), name='notepad_list'),
    path('pad/<int:id>/',NotePadDetailView.as_view(), name='notepad_detail'),
    path('pad/add/',NotePadAddView.as_view(), name='notepad_add'),
    path('pad/edit/<int:id>',NotePadEditView.as_view(), name='notepad_edit'),
    path('pad/delete/<int:id>',NotePadDeleteView.as_view(), name='notepad_delete'),
]