import requests
import re
from bs4 import BeautifulSoup as bs
from matplotlib import pyplot as plt

y_ = []
y = []
x = ['无双','我的间谍前男友','找到你']
pattern = '.*?总票房明细">(.*?)</a>.*?'
for i in range(3,6):
    a=0
    url = ("http://58921.com/boxoffice/wangpiao/2018102" + str(i))
    res = requests.get(url)
    html = str(res.content,"utf-8")

    soup = bs(html,'lxml')
    for i in soup.select('tr'):
        m = i.select('td:nth-of-type(2) a')
        if m == []:
            continue
        else:
            pf = re.findall(pattern,str(m))
            y_.append(str(pf)[2:-2])
        a+=1
        if a == 3:
            break
for i in y_:
    if i[-1:] == "万":
        y.append(float(i[:-1])/10000)
    else:
        y.append(float(i[:-1]))
print(y)
x_1 = list(range(len(x)))
x_2 = [i+0.2 for i in x_1]
x_3 = [i+0.2*2 for i in x_1]
plt.figure(figsize=(20,8),dpi=80)
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.yticks(x_2,x)
plt.xlabel('票房/亿')
plt.ylabel('电影名称')
plt.title('10月23到25号票房统计')

plt.barh(x_1,y[:3],height=0.2,label = "10月23号")
plt.barh(x_2,y[3:6],height=0.2,label = "10月24号")
plt.barh(x_3,y[-3:],height=0.2,label = "10月25号")
plt.legend()

plt.show()



