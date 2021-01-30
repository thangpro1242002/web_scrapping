
# Các thư viện cần thiết
import os
import requests

# Hàm Tạo thư mục và chuyển đến thư mục đó
# Cần truyền vào cho hàm Tên thư mục
def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)


#Hàm này để lưu lại các đường dẫn đã lấy vào thư mục vừa tạo
def luu_file(data, name_folder):
    #data là list chứa nội dung file html
    path = "C:\Users\Admin\Desktop\web_scrapping"
    os.chdir(path + str(name_folder))









    
