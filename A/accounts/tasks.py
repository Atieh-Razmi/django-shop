from celery import shared_task
from accounts.models import OtpCode
from datetime import datetime,timedelta
import pytz

@shared_task
def remove_expired_otp_codes():
    expired_time = timedelta.now(tz=pytz.timezone('Asia/Tehran')) - datetime(minute=2)
    OtpCode.objects.filter(created__lt==expired_time).delete()