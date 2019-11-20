# from PIL import Image
# import requests
# from io import BytesIO
#
#
#
# #url="https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwizzYiS3vXlAhUGLo8KHS3vDToQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.migrationsverket.se%2FEnglish%2FPrivate-individuals%2FEnclose-copy-of-your-passport-with-your-application.html&psig=AOvVaw0HKZB5mDrXBzbefUhKqHE5&ust=1574234359668934"
#
# # response = requests.get(url)
# # img = Image.open(BytesIO(response.content))
# from PIL import Image
# import urllib.request
#
# URL = 'https://storage.cloud.google.com/keelaa-images/Treck/ganesh8/IMG_20190914_062840.jpg'
#
# with urllib.request.urlopen(URL) as url:
#     with open('temp.jpg', 'wb') as f:
#         f.write(url.read())
#
# img = Image.open('temp.jpg')
#
#
# img.show()
import re
from collections import Counter
l=[100,200,300,400,500,600, 700,15001]
max_num =max(l)/5000
abc =str(max_num).split('.')

if re.search('[1-9]',abc[1]):
    max_num=int(abc[0])+1
d = Counter(l)
intial=0
final=5000
li=[]
for x in range(max_num):
    if intial >=5000:
        intial =final-4999
    print("intial,final",(intial,final))
    d2=[x for x in range(intial,final+1)]
    li.append(d2)
    if max in d2:
        break

    intial =intial+5000
    final =final+5000


print(li)

        # print(sum (dic.values()))
