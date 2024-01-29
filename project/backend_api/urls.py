from django.urls import path

from .v1.views import (CustomersView, PoliciesView,PoliciesDetailView,QuotesView)

urlpatterns = [


    path('v1/create_customer/', CustomersView.as_view(), name="Create Customer"),
    path('v1/quote/', QuotesView.as_view(), name="quote"),
    path('v1/policies/', PoliciesView.as_view(), name="policies"),
    path('v1/policies/<str:pk>/', PoliciesDetailView.as_view(), name="policies-detail"),

]