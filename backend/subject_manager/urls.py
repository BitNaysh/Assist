from django.urls import path
from .views import get_assignments, create_assignment, update_assignment, delete_assignment

urlpatterns = [
    path('assignments/', get_assignments, name='get_assignments'),
    path('assignments/create/', create_assignment, name='create_assignment'),
    path('assignments/<int:pk>/update/', update_assignment, name='update_assignment'),
    path('assignments/<int:pk>/delete/', delete_assignment, name='delete_assignment'),
]
