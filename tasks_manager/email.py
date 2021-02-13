from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.conf import settings


def send_alert_email_for_match(match, recipient_list, host_values):
    context = {'username': "alex",
               'pk': str(match.id),
               'match': str(match),
               'scheme': str(host_values.get('scheme')),
               'host': str(host_values.get('host'))}

    template = 'tasks_manager/alert_email.html'

    email_subject = "Invitation"
    email_body = render_to_string(template, context=context)
    import pdb
    pdb.set_trace()
    email = EmailMessage(
        email_subject,
        email_body,
        settings.EMAIL_HOST_USER,
        recipient_list
    )
    email.send()
