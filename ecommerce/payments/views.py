from django.shortcuts import render
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripePaymentView(APIView):
    def post(self, request):
        try:
            # Get amount and payment method from the request
            amount = int(request.data.get('amount')) * 100  # Stripe works in cents
            payment_method_id = request.data.get('payment_method_id')

            # Create a payment intent on Stripe
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                payment_method=payment_method_id,
                confirmation_method='manual',
                confirm=True,
            )

            return Response({'client_secret': intent.client_secret}, status=status.HTTP_200_OK)
        except stripe.error.CardError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
