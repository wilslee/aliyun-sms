# usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

## 安装阿里云通信 SDK
aliyunsdkcore_dir = os.path.join(here, 'sdk/aliyun-python-sdk-core/')
aliyunsdkdysmsapi_dir = os.path.join(here, 'sdk/aliyun-python-sdk-dysmsapi/')

sys.path.extend([aliyunsdkcore_dir, aliyunsdkdysmsapi_dir])
