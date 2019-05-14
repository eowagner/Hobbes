from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_game, name='create'),
    path('instructor_view/<int:instance_id>/', views.instructor_view, name="instructor_view"),
    path('close/<int:instance_id>', views.close_instance, name="close_instance"),
    path('delete_response/<int:instance_id>/<int:response_id>', views.delete_response, name="delete_response"),
    path('play/<int:instance_id>/', views.play_game, name='play_game'),
    path('anon_results/<int:instance_id>/', views.anon_results, name='anon_results'),
    path('delete_instance/<int:instance_id>/', views.delete_instance, name='delete_instance')
]
