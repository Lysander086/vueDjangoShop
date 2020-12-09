import re
from datetime import datetime, timedelta

from future.backports.datetime import timedelta
from rest_framework import serializers
from django.contrib.auth import get_user_model
from MxShop.settings import REGEX_MOBILE
from users.models import VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """验证手机号码
            :param mobile

        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 手机号是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码非法')

        # 60s内只能发送一次
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile

# class UserSerializer(serializers.ModelSerializer):

