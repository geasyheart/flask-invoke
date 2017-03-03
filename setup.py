from distutils.core import setup

setup(
    name='flask-invoke',
    version='0.0.1',
    packages=['invoke', 'invoke.services'],
    url='none',
    license='GPL3',
    author='yu.zhang',
    author_email='geasyheart@163.com',
    description='微服务注册与发现-invoke',
    install_requires=[
        'requests==2.13.0',
    ]
)
