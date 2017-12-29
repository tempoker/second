import requests
#import urllib.request as ur
from lxml import etree
#这是不需要验证码的提交post表单案例
s = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',\
           'Referer':'https://www.hellobi.com/',\
           'Connection':'keep-alive','Content-Type':'text/html; charset=UTF-8',
           }
'''
html = s.get(url)
print(len(html.content))
data = etree.HTML(html.content)
captcha=data.xpath("//img[@id='verifyPic_login']/@src")
if len(captcha)>0 :
     print('OMG还有验证码！！')
     file = 'yanzhengma.png'
     ur.urlretrieve(captcha[0],file)
     captcha_value = input('请查看那本地验证码！并输入：')
'''
url = 'https://passport.hellobi.com/sso/login'
data = {"username": "1578852802@qq.com", "password": "Yanhu20131105"} 
rst = s.post(url,data,headers) #通过post传参登录，重在获取cookies
url2 ='https://www.hellobi.com/u/91791' #登录后跳转到页面,个人中心
#cookies={'XSRF-TOKEN': 'eyJpdiI6InNOQTE1dG40VnVxaFdoQm5Vb3hnbWc9PSIsInZhbHVlIjoiM1wvbTkreTZDRE9kVm5PSzg5TWNGd2tCWW1iZk8zTlFHa3VWbjluY1FQNTJiV3Z0UmFwV21NY28wcXY5ZEZZRHRWRTVPOFhoYmZQZFN2Zjk4YzZzTjFRPT0iLCJtYWMiOiJkMTExNTIzN2RmMDk2NTI0ZGE3YTAwZWM3NjNiN2ZkMDJjMTY5ODZhY2ZjMjFjMTk5MmMzYmNmNWNiYTUyY2Q4In0%3D', 'laravel_session': 'eyJpdiI6IllNOEtoWmk3T09yNzRVSjd1MVNsMFE9PSIsInZhbHVlIjoiWnJ2TTBBd1ViXC8zeTRLMXcwem9sN0lDbkhxRmJPVlV1THo2NzZscU1ndVdudkhoSExqV3pVU2V3Z1F0NGRreTI2OXc1UVhrUlRPSU1nRUtFV2hDQlhnPT0iLCJtYWMiOiJiZDBjOGQ2MzcwNTMyNDhiMjU2NzdiMzlmZjllMmRhZDc1Nzg5MGMwOGRiNzI3ZGEwYTE1MTUyNzlhM2JmNjA3In0%3D'}
#从network中所有set_cookie找第一个分号前的内容。组成的字典。
html3 = s.get(url2,cookies=rst.cookies,headers=headers)
data3 =etree.HTML(html3.content) 
title = data3.xpath('/html/head/title/text()')[0]
name = data3.xpath('//div[@class="col-md-7 info"]/h2/text()')[0]
time = data3.xpath('//div[@class="col-md-7 info"]/p[2]/text()')[0]
#/html/body/div[2]/div/div/div[2]/p[2] 这是复制浏览器提供的xpath表达式，根标签出发
print(title)
print(name.strip()+':'+time)
'''
from selenium import webdriver as wdr
from lxml import etree
from time import sleep
from random import rnadint as r
import numpy as npy
from sklearn.externals.six import StringIO
from sklearn.tree import DecisionTreeClassifier as DTC
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from sklearn.tree import export_graphviz #可视化输出
url = ''
bs = wdr.PhantomJS()
bs.get(url)
sleep(3+r(1,10)/float(10))
bs.save_screenshot('weibo.png')
bs.get_screenshot_as_file('jingd.gif')
html = bs.page_source
data = etree.HTML(html)
bs.quit()
'''
'''
with open('weibo.html','w',encoding='utf-8') as fh:
     print(len(html))
     fh.write(str(html))
'''
'''
fname = 'D:\\Python36...'
with open(fname,encoding='utf-8') as fh:
     html = fh.read() #也可以按行读取 fh.readline()
     print(len(html))
data = etree.HTML(html)
'''
'''
labels = []#存储标签（结果）
comment = data.xpath("//p[@class='comment_txt']")
train_num = int(len(comment)*0.8)#抽取80%数据作为训练数据
for i in range(train_num):#如<p class='comment_txt'>还不回来<span>我们不一样</span></p>
     info = comment[i].xpath('string(.)') #把p标签下的所有文本[还不回来，我们不一样]取出来
     if info:
     print('第'+str(i+1)+'条评论内容是：')
     print(info.strip())
     thislabel = input('请输入此微博[0-负向 1-正向 2-中性]感情类别： ')
     labels.append(thislabel)
'''
'''
import jieba
cutdata = [] #语料库
for i in range(len(comment)): #对每条评论进行切词，拼成
     info = comment[i].xpath('string(.)')#把出现的标签看成空白
     thiscut = jieba.cut(info)
     thiscutdata = ''
     for j in thiscut:
          thiscutdata += j+' '
     cutdata.append(thiscutdata)
'''
'''
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(cutdata)
alltz = x.toarray() #把全部数据转化为数组
traindata = alltz[0:train_num,:]#取训练数据
trainlabels = labels.copy()
#建立决策树
dtc = DTC(criterion='entropy')
dtc.fit(traindata,trainlabels)
testdata = alltz[train_num:,:]#测试数据
rst = dtc.predict(testdata)
print(rst) #以下是做可视化
with open('motion.bot','w') as fh:
     export_graphviz(dtc,feature_names=['acombat','lesson','promo','datum'],out_file=fh)
#使用人工神经网络模型
model = Sequential()
model.add(Dense(10,input_dim=len(traindata[0]))) #每个结果对应的特征量数目
model.add(Activation='relu')
model.add(Dense(1,input_dim=1))
model.add(Activation('sigmoid'))
model.compile(loss='mean_squared_error',optimizer='adam')
model.fit(traindata,trainlabels,epochs=200,batch_size=100)#训练建模
testdata =alltz[train_num:,:]#测试数据,直接进行预测
rst = model.predict_classes(testdata).rehsape(len(testdata))#多少个结果
print(rst)
'''
