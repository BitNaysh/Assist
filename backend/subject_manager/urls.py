from django.urls import path
from .views import (
    AssignmentItemViews,
)

urlpatterns = [
    path('assignment/', AssignmentItemViews.as_view()),
]
