from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .pdf_generator import generate_invoice
from django.core.mail import EmailMessage

class OrderView(APIView):
    def post(self, request):
        # Logic for creating an order
        order = Order.objects.create(
            user=request.user,
            total_amount=request.data.get('total_amount')
        )

        # Generate the invoice PDF
        pdf_path = generate_invoice(order)

        # Send the PDF via email
        email = EmailMessage(
            'Your Invoice',
            'Thank you for your order. Please find your invoice attached.',
            'from@example.com',
            [order.user.email],
        )
        email.attach_file(pdf_path)
        email.send()

        return Response({'message': 'Order created and invoice sent!'})
