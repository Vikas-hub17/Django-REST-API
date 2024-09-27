from django.urls import path
from .views import StripePaymentView

urlpatterns = [
    path('stripe/', StripePaymentView.as_view(), name='stripe-payment'),
]
