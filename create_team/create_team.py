#coding:utf-8
import urllib2,urllib
import cookielib
import re, json ,time
import os, commands

email_name = "test_mail%s@qq.com" % time.time()
url='http://192.168.1.16:8080'

#--------------------------------------注册申请
add_mail = {"password": "123456", "email": email_name}
 #{"email": "152105966@139.com", "password": "123456"}

#将要POST出去的数据进行编码
opener = urllib2.build_opener()
data = json.dumps(add_mail)  #提供数据缓存的application/x-www-form-urlencoded格式
response = urllib2.Request(url+"/api/user/account", data,headers={'Content-Type': 'application/json'})
add_mail = opener.open(response)
print "[websocke] send is \t" + data
print "[websocke] res is \t" + add_mail.read()

#--------------------------------激活邮件
os.system("sh get_mail_token.sh %s" % email_name)
x = os.popen("cat %s" % email_name ).read()
token = re.sub(re.compile(".*token="), "", x) #mail名称
token = re.sub(re.compile("\n"), "", token) #结尾换行
print "mail is %s, token is %s" % (email_name, token)
#创建一个cj的cookie的容器
cj = cookielib.CookieJar()
opener_cj = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
add_login = {"token": token,"email": email_name,"terminal_type":"browser","device":{"os":"Windows","version":"7","model":"Chrome","device_id":"IMEI|MEID|ESN|UUID|MAC"}}
add_login_data = json.dumps(add_login)
res = urllib2.Request(url+"/api/user/activate",add_login_data, headers={'Content-Type': 'application/json'})

log_mail = opener_cj.open(res)
print "*" * 20
res = log_mail.read()
print "[websocke] send is \t" + add_login_data
print "[websocke] res is \t" + res
res = json.loads(res)
print type(res)
#[next] 判断返回结果是否正常
if (0 == res["result"] ):
    host_id = res["tid"]
    tstoken = res["tstoken"]
    print "host_id is %s, tstoken is %s" % (host_id, tstoken)
