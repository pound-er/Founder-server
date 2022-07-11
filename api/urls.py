from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('type/recommend/', views.Type4RecommendView.as_view()),
]
