from django.core.mail import send_mail
from django.conf import settings

def send_forgetpassword_mail(user,token):
  subject="Your reset password link"
  message=f"Hi ,click on this link for reset your password http://localhost:8000/resetpassword/{token}"
  email_from = 'pappuraj.webit@gmail.com'
  recipient_list = [user.email,]
  send_mail(subject, message, email_from, recipient_list)
  return True
