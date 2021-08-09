import requests
from bs4 import BeautifulSoup
import csv
import json

response = requests.get("http://paullab.synology.me/stock.html")

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

oneStep = soup.select('.main')[2]
twoStep = oneStep.select('tbody > tr')[1:]

날짜 = []
종가 = []
전일비 = []
거래량 = []

for i in twoStep:
  날짜.append(i.select('td')[0].text)
  종가.append(int(i.select('td')[1].text.replace(',', '')))
  전일비.append(int(i.select('td')[2].text.replace(',', '')))
  거래량.append(int(i.select('td')[6].text.replace(',', '')))

l = []

for i in range(len(날짜)):   # 날짜의 Length(len) 만큼 돌면서
  l.append({
      '날짜':날짜[i],     # 날짜의 [i] 번째에 있는데이터를 딕셔너리형태로 l 에다가 append 해준다
      '종가':종가[i],     # 종가의 [i] 번째에 있는데이터를 딕셔너리형태로 l 에다가 append 해준다
      '전일비':전일비[i], # 전일비의 [i] 번째에 있는데이터를 딕셔너리형태로 l 에다가 append 해준다
      '거래량':거래량[i], # 거래량의 [i] 번째에 있는데이터를 딕셔너리형태로 l 에다가 append 해준다
  })
l

#파일을 한 번 쓴다
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
  json.dump(l, f_write, ensure_ascii=False, indent=4)

# 파일을 다시 읽는다
data = ""
with open('data.js', "r", encoding="UTF-8-sig") as f:
  line = f.readline()
  while line:
    data += line
    line = f.readline()

# 파일에 변수명을 추가하여 다시쓴다.
final_data = f"var data = {data};"
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
  f_write.write(final_data)
