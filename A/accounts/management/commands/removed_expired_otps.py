from typing import Any
from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime,timedelta
import pytz

class Command(BaseCommand):
    help='remove all expire otp codes'

    def handle(self, *args, **options):
        expired_time = timedelta.now(tz=pytz.timezone('Asia/Tehran')) - datetime(minute=2)
        OtpCode.objects.filter(created__lt==expired_time).delete()
        self.stdout.write('all expired otp codes removed')

        