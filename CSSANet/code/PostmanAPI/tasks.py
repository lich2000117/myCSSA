from celery.app import task
from celery.schedules import schedule
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from .models import MailDraft, MailQuene


@task(name='send_mail_in_plain_text')
def send_mail_in_plain_text(mail_body_id:str, ):
    
    return


@task(name='send_mail_with_http_template')
def send_mail_with_http_template(mssage:EmailMultiAlternatives):
    
    return 
