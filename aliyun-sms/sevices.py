# usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import json
from django.conf import settings
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkcore.client import AcsClient

REGION = "cn-hangzhou"
ACCESS_KEY_ID = getattr(settings, 'ALIYUN_ACCESS_KEY_ID', '')
ACCESS_KEY_SECRET = getattr(settings, 'ALIYUN_ACCESS_KEY_SECRET', '')

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)


def dict_to_str(dict_obj):
    return json.dumps(dict_obj)


def send_sms(business_id, phone_numbers, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)

    # 短信模板变量参数
    if template_param is not None:
        if isinstance(template_param, dict):
            template_param = dict_to_str(template_param)
        smsRequest.set_TemplateParam(template_param)

    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)

    # 短信签名
    smsRequest.set_SignName(sign_name)

    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)

    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)

    # TODO 业务处理

    return smsResponse


def test_send_sms(phone='18319079676'):
    sign_name = '阿里云短信测试专用'
    template_code = 'SMS_73105023'
    params = {'customer': "短信测试员"}
    return send_sms(uuid.uuid1(), phone, sign_name, template_code, params)

