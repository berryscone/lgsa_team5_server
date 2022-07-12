from django.urls import path, include

from knox import views as knox_views

from .health import HealthCheckCustomView

from vehicle_query_app.views import LoginView

urlpatterns = [
    path('', include('vehicle_query_app.urls')),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('health/', HealthCheckCustomView.as_view()),
]
