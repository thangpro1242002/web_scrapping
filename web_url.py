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
def kiem_tra_duong_dan(url):
    check = re.search("^http", url)
    try:
        if url == check.string:
            return True
    except:
        return False        
        
#Hàm này để chỉnh sửa đường dẫn chưa hợp lệ
def chinh_sua_duong_dan(url, item): 
    item = str(url) + item    #Thêm https://... vào
    return item


