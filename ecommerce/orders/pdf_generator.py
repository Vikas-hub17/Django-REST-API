from django.template.loader import get_template
from weasyprint import HTML
from django.conf import settings
import os

def generate_invoice(order):
    # Load the invoice template
    template = get_template('invoice_template.html')
    context = {
        'order': order,
        'user': order.user,
        'items': order.items.all(),
    }
    html = template.render(context)

    # Generate the PDF from HTML
    pdf_file = HTML(string=html).write_pdf()

    # Save the PDF to a file
    pdf_path = os.path.join(settings.MEDIA_ROOT, f'invoices/invoice_{order.id}.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(pdf_file)

    return pdf_path
