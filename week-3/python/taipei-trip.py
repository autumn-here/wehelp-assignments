import urllib.request as request  # 載入python網路連線模組
import json  # 內建解讀json格式的模組

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(src) as response:
  data=json.load(response)
# print(data)

dataList = data["result"]["results"]

with open("data.csv", "w", encoding="utf-8") as file:
  for attraction in dataList:
    info = []
    info.append(attraction["stitle"])  #景點名稱
    info.append(attraction["address"][5:8]) #行政區
    info.append(attraction["longitude"])  #經度
    info.append(attraction["latitude"])   #緯度
    index = attraction["file"].find(".jpg")  #(定位第一個.jpg的index)
    info.append(attraction["file"][0:(index+4)])  #封面圖片網址
    file.write((",").join(info)+"\n")