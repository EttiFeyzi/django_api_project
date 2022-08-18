from datetime import datetime
from kavenegar import *
from config.settings import Kavenegar_API 
from random import randint
import datetime
from .models import MyUser


def send_otp(mobile, otp):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = { 
            'sender':'1000596446',
            'receptor': mobile,
            'messege': 'Your OTP is {}'.format(otp),
            
        }
        response = api.sms_send(params)
        print('otp:', otp)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return randint(1000, 9999)


def chek_otp_expiration(mobile):
    try:
        user = MyUser.objects.get(mobile=mobile)
        now = datetime.datetime.now()
        otp_time = user.otp_create_time
        diff_time = now-otp_time
        print('OTPTIME: ', diff_time)

        if diff_time.seconds > 30:
            return False
        return True

    except MyUser.DoesNotExist:
        return False
