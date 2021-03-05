import urllib.request
import urllib.parse
import json
import time

'''
head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
'''

while True:
    content=input("请输入需要翻译的内容（输入q退出程序）:")
    if content=='q':
        break
    
    
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data={}
    data['from']='AUTO'
    data['to']='AUTO'
    data['i']=content
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='16109634771629'
    data['sign']='0d5be2419cba9d638c8e045b13c60f5e'
    data['lts']='1610963477162'
    data['bv']='e65e8e5642f3c2d719d32db0b5eff1f9'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_CLICKBUTTION'
    data=urllib.parse.urlencode(data).encode("utf-8")


    req=urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36')
 
    response=urllib.request.urlopen(req)
    html=response.read().decode("utf-8")
 
    target=json.loads(html)
    print("翻译结果:%s" % (target['translateResult'][0][0]['tgt']))
    time.sleep(5)
