import web_url
import luu_url

def start():
    home_page = input("nhap link :")  #trang chủ để chứa các đường link
    url_list = history = []  # DS các đường dẫn đã duyệt
    max_page =int(input("nhập số trang bạn muốn tải:"))  #Nhập số lượng trang web mà bạn muốn tải
    count = 0  # đếm số lượng trang web đã tải về
    data_folder = "C:\\webscrapping\\"
    # Tạo Folder
    folder.tao_thu_muc(data_folder)
    url_list.append(home_page) #thêm đường link mình nhập từ domain vào list url_list
    # kịch bản tải các trang web
    while (count < max_page) and (len(url_list) > 0):   #sử dụng vòng lặp while với điều kiện biến đếm phải nhỏ hơn số lượng của page và độ dài của link phải lớn hơn 0
        url = url_list.pop(0)  # Lấy phần tử đầu tiên của url_list
        history.append(url)  # thêm phần tử vào history
        # Đọc nội dung
        data = web_url.doc_noi_dung(url) 
        # Lấy tất cả đường dẫn
        item = web1.lay_duong_dan(content)
        for i in item:
        if web1.kiem_tra_duong_dan(i) == False:   ## Kiểm tra đường dẫn
            i = web_url.chinh_sua_duong_dan(url_first, i)       
        if (i not in history) and (i not in url_list):
            if web_url.kiem_tra_url_da_duyet(i) == True:
                continue    
            else:    
                url_new.append(i)       ###Thêm đường dẫn hợp lệ vào url_new
        # đếm số đường dẫn đã duyệt
        count += 1
      
if __name__ == '__main__':
    start()
