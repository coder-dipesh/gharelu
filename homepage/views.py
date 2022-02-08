from django.shortcuts import redirect, render
from authentications.auth import customer_only
from homepage.forms import OrderForm
from homepage.models import Order
from professionals.models import Service
from .filters import ServiceFilter
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages

def homepage(request):
    return render(request,'homepage/homepage.html')

def about(request):
    return render(request,'homepage/about.html')


def service(request):
    services = Service.objects.all().order_by('-id')
    service_filter = ServiceFilter(request.GET, queryset=services)

    services_final = service_filter.qs 

    context = {'services':services_final , 'service_filter':service_filter}
    return render(request,'homepage/service.html',context)

def review(request):
    return render(request,'homepage/review.html')

def error404(request, exception):
    return render(request,'error404.html')



@login_required
@customer_only
def bookService(request, service_id):
    user = request.user
    services = Service.objects.get(id=service_id)
    service = Service.objects.get(id=service_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            price = services.service_price
            contact_no = request.POST.get('contact_no')
            contact_address = request.POST.get('contact_address')
            date = request.POST.get('date')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')

            order = Order.objects.create(service=services,
                                        user=user,
                                        contact_no=contact_no,
                                        contact_address=contact_address,
                                        date=date,
                                        start_time=start_time,
                                        end_time=end_time,
                                        total_price=price,
                                        status="Pending"
                                        )
            if order:
                template = render_to_string('homepage/email_templates.html',
                                            {'name': request.user.username, 'service': services.service_name,'date':date, 'time1':start_time, 'time2':end_time})
                email = EmailMessage(
                    'Thank you for choosing Gharelu!!',
                    template, settings.EMAIL_HOST_USER, [request.user.email],
                )
                email.fail_silently = False
                email.send()
                messages.add_message(request, messages.SUCCESS, 'Service Ordered Successfully!!')
                return redirect('/customers/my_bookings')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'homepage/bookServiceForm.html', {order_form: form})

    context = {
        'order_form': OrderForm,
        'services': services,
        'service': service,
    }
    return render(request,'homepage/bookServiceForm.html',context)



def cancelBookingService(request, service_id):
    service = Order.objects.get(id=service_id)
    service.delete()
    messages.add_message(request, messages.SUCCESS, 'Service cancelled successfully!!')
    return redirect('/customers/my_bookings')



