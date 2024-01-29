from django.urls import path

from . import views
app_name="accounts"
urlpatterns = [
    path("auth/", views.GetKeycloakToken.as_view(), name="get_user_token"),
    path("refresh-token/", views.GetKeycloakRefresh.as_view(), name="get_refresh_token"),


]