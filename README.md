# aliyun-sms
原阿里云通信的 Python SDK 是 Python2 版本

在公司使用中，项目是用 Python3, 使用 future 改造为 Python3版本


### 安装
```
>> python setup.py install
```

### 使用

```
from aliyunsms.services import AliyunSMSClient

if __name__ == '__main__':
    client = AliyunSMSClient('AliyunAccessKeyId', 'AliyunAccessKeySecret')
    client.send_sms('手机号码', '短信签名', '模版ID', 模版参数)
    client.test_send_sms('手机号码')
```
