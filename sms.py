from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def send():
    client = AcsClient('LTAI4G4p84FtAuZdqaabT1Li', 'SZRrl5EbmS726NS4U1foHYiXHDkCD8', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', "17863698891")
    request.add_query_param('SignName', "练习用项目的验证码")
    request.add_query_param('TemplateCode', "SMS_203190819")
    request.add_query_param('TemplateParam', "{code:1111}")
    response = client.do_action(request)

    # python2:  print(response)
    print(str(response, encoding = 'utf-8'))

