
# Các thư viện cần thiết
import os
#Hàm tạo thư mục 
def tao_thu_muc(path):
    os.chdir(path)  #Di chuyển đến thư mục trong đường dẫn path
    os.mkdir('webscrapping')

    #Tạo file History.txt trong webscrapping
    path = 'C:\\webscrapping\\'
    os.chdir(path)  # Di chuyển đến thư mục trong đường dẫn path
    file = open("History.txt", "w", encoding="utf-8")
    for item in content:
        file.write(item)
    file.close()




#Hàm này để lưu lại các đường dẫn đã lấy vào thư mục vừa tạo
def luu_file(data, name_folder):
    #data là list chứa nội dung file html
    path = "C:\\webscrapping\\"
    os.chdir(path + str(name_folder))









    
