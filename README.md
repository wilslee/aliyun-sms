# aliyun-sms
原阿里云通信的 Python SDK 是 Python2 版本

在公司使用中，项目是用 Python3, 使用 future 改造为 Python3版本


### 安装
```
    >> python setup.py install
```

### 使用

```
from aliyunsms.services import BaseClient

if __name__ == '__main__':
    client = BaseClient('AliyunAccessKeyId', 'AliyunAccessKeySecret')
    client.send_sms(phone_numbers, sign_name, template_code, template_param)
    client.test_send_sms('YourPhone')
```
