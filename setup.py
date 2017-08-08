"""
"""
import os
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

## 安装阿里云通信 SDK
aliyunsdkcore_dir = os.path.join(here, 'aliyunsms/sdk/aliyun-python-sdk-core/')
aliyunsdkdysmsapi_dir = os.path.join(here, 'aliyunsms/sdk/aliyun-python-sdk-dysmsapi/')
os.system('cd {} && python setup.py install'.format(aliyunsdkcore_dir))
os.system('cd {} && python setup.py install'.format(aliyunsdkdysmsapi_dir))
# os.system('cd {}'.format(here))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aliyunsms',
    version='0.0.1',
    description='Aliyun SMS',
    long_description=long_description,
    url='https://github.com/wilslee/aliyun-sms',
    author='wilslee',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: SMS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='aliyun sms development',
    include_package_data=True,
    platforms="any",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['django', 'future'],
)
