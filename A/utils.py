from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('4F786B4456763461586C42324D6A6A687A4B3548734A6739747673653054426D4D4D44714271637341576F3D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'کد تایید شما {code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)

class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin        