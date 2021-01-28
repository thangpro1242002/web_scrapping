import web_url
import luu_url

def main():
    url_goc=input("Nhập link khởi đầu:")
    

    #Kịch bản tải các trang web
    while (count < max_page) and (len(url_list) > 0):
        url = url_list.pop(0)
        page = web_op.doc_noi_dung(url)
        links = web_op.lay_cac_duong_link(page)
        for item in links: #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if web_op.kiem_tra_link(item): #Nếu đường link là hợp lệ thì tiếp tục thuwucj hiện đoạn lệnh bên dưới
                item = web_op.chinh_sua_link(item)  #Chỉnh sửa nếu thiếu phần https://...
                if not((item in url_list) and (item in history)):  #Nếu đường link chưa hề được duyệt và chưa có trong hàng đợi
                    url_list.append(item) #Thêm đường link mới vào danh sách chờ duyệt
        folder_op.luu_noi_dung_xuong_file(page, data_folder)
        history.append(url)
        count += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
