# usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import json
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkcore.client import AcsClient

REGION = "cn-hangzhou"

class BaseClient(object):

    region = "cn-hangzhou"
    client = None

    def __init__(self, key_id, key_secret, region=None):
        self.key_id = key_id
        self.key_secret = key_secret
        if region is not None:
            self.region = region
        self.client = AcsClient(self.key_id, self.key_secret, self.region)

    def send_sms(self, phone_numbers, sign_name, template_code, template_param=None):
        if isinstance(phone_numbers, (list, tuple)):
            phone_numbers = ','.join(phone_numbers)

        smsRequest = SendSmsRequest.SendSmsRequest()
        # 申请的短信模板编码,必填
        smsRequest.set_TemplateCode(template_code)
        # 短信模板变量参数
        if template_param is not None:
            if isinstance(template_param, dict):
                template_param = json.dumps(template_param)
            smsRequest.set_TemplateParam(template_param)

        # 设置业务请求流水号，必填。
        smsRequest.set_OutId(uuid.uuid1())
        # 短信签名
        smsRequest.set_SignName(sign_name)
        # 短信发送的号码列表，必填。
        smsRequest.set_PhoneNumbers(phone_numbers)
        # 调用短信发送接口，返回json
        smsResponse = self.client.do_action_with_exception(smsRequest)
        return smsResponse

    def test_send_sms(self, phone):
        sign_name = '阿里云短信测试专用'
        template_code = 'SMS_73105023'
        params = {'customer': "短信测试员"}
        return self.send_sms(phone, sign_name, template_code, params)


class AliyunSMSClient(BaseClient):
    pass