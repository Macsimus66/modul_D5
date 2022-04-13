from django.shortcuts import render, redirect, reverse
from django.views import View
from datetime import datetime
from .models import Appointment
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        html_content = render_to_string(
            'appointment_created.html',
            {
                'appointment': appointment,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            body=appointment.message,
            from_email='peterbadson@yandex.ru',
            to=['skavik46111@gmail.com'],
        )
        msg.attach_alternative(html_content, "text/html")

        msg.send()

        return redirect('appointments:make_appointment')

    def notify_managers_appointment(sender, instance, created, **kwargs):
        if created:
            subject = f'{instance.client_name} {instance.date.strftime("%d %m %Y")}'
        else:
            subject = f'Appointment changed for {instance.client_name} {instance.date.strftime("%d %m %Y")}'

        mail_managers(
            subject=subject,
            message=instance.message,
        )

    post_save.connect(notify_managers_appointment, sender=Appointment)