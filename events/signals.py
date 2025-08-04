from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Event

@receiver(m2m_changed, sender=Event.participants.through)
def send_rsvp_confirmation_email(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == "post_add" and not reverse:
        for user_pk in pk_set:
            user = model.objects.get(pk=user_pk)
            event = instance

            mail_subject = f'RSVP Confirmation for {event.name}'
            message = render_to_string('emails/rsvp_confirmation.html', {
                'user': user,
                'event': event,
            })
            to_email = user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
