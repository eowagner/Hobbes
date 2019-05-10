from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_game, name='create'),
    path('instructor_view/<int:instance_id>/', views.instructor_view, name="instructor_view"),
    path('instructor_view/<int:instance_id>/<int:response_id>', views.instructor_view, name="delete_response"),
    path('instructor_view/close/<int:close_id>', views.instructor_view, name="close_instance"),
    path('play/<int:instance_id>/', views.play_game, name='play_game'),
    #path('online_test/', views.online_test, name="online_test"),
    path('anon_results/<int:instance_id>/', views.anon_results, name='anon_results'),
]
