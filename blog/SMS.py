import random
import sys
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT

ACCESS_KEY_ID = "LTAIDHOYSjYcvyVt"  #用户AccessKey  需要根据自己的账户修改
ACCESS_KEY_SECRET = "qrEgykmXX4e6GUMFOqzuiLZ5gsUxSC"  #Access Key Secret  需要根据自己的账户修改

try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:
    pass
except Exception as err:
    raise err

# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)

class SMS:
    def __init__(self,signName,templateCode):
        self.signName = signName  #签名
        self.templateCode = templateCode  #模板code
        self.businessID = uuid.uuid1()

    def send(self,phone_numbers,template_param):
        smsRequest = SendSmsRequest.SendSmsRequest()
        # 申请的短信模板编码,必填
        smsRequest.set_TemplateCode(self.templateCode)

        # 短信模板变量参数
        if template_param is not None:
            smsRequest.set_TemplateParam(template_param)

        # 设置业务请求流水号，必填。
        smsRequest.set_OutId(self.businessID)

        # 短信签名
        smsRequest.set_SignName(self.signName)

        # 数据提交方式
        # smsRequest.set_method(MT.POST)

        # 数据提交格式
        # smsRequest.set_accept_format(FT.JSON)

        # 短信发送的号码列表，必填。
        smsRequest.set_PhoneNumbers(phone_numbers)

        # 调用短信发送接口，返回json
        smsResponse = acs_client.do_action_with_exception(smsRequest)

        return smsResponse


if __name__ == "__main__":
    sms = SMS("成少雷","SMS_102315005")
    phone = input("请输入手机号：")
    #验证码
    num = random.randint(10000,99999)

    para = "{'number':'%d'}"%num
    res = sms.send(phone,para)
    print(res.decode('utf-8'))