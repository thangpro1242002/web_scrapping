# Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
import re

#Hàm này dùng để đọc nội dung đường dẫn
#Kết quả trả về là nội dung trong đường dẫn
def doc_noi_dung(url):
    page = requests.get(url).text    #Gửi yêu cầu truy cập url
    content = BeautifulSoup(page, 'html.parser')
    return content

#hàm lấy các đường link web trong các nội dung đọc về
#Kết quả trả về là một DS chứa các đường dẫn
def lay_duong_dan(content):
    result = []
    raw = content.find_all("a")     #Lọc các thẻ <a>
    for item in raw:
        link = item.get("href")     #Lấy ra các đường dẫn trong href
        result.append(link)
    return result


