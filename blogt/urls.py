from django.urls import path
from .import views
urlpatterns = [
    path('', views.PostlistViews.as_view(), name='blog'),
    path('<int:pk>/', views.DetailPostViews.as_view(), name='post detail'),
    path('create/', views. CreatPostView.as_view(), name='newpost'),
    path('<int:pk>/update/', views.UpdateListView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeletePostViewes.as_view(), name='delete')
]

