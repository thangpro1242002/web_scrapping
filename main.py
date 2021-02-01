import folder, web

# Kịch bản

# Nhập đường dẫn, giới hạn page tải về
url_first = input("Nhập đường dẫn:")
n = int(input("Nhập giới hạn page: "))
# Tạo các danh sách
url_list = []  # DS các đường dẫn chưa duyệt
url_list_limit = 5000
history = []  # DS các đường dẫn đã duyệt
max_pages = n
folder.kiem_tra_folder("C:\\")  # Kiểm tra và tạo thư mục CRAWLER để lưu trữ
data_folder = 'C:\\CRAWLER'  # Lưu vào ổ C thư mục CRAWLER
count = 0
# Thêm url vào hàng chờ
url_list.append(url_first)
# Tạo Folder
folder.kiem_tra_folder(data_folder)
while count < max_pages:
    url = url_list.pop(0)
    # danh sách những đường dẫn vừa tìm được
    url_new = []
    url_new_limit = 1000
    # Đọc nội dung
    content = web.doc_noi_dung(url)
    # Lấy tất cả đường dẫn
    item = web.lay_duong_dan(content)
    for i in item:
        if web.kiem_tra_duong_dan(i) == False:  ## Kiểm tra đường dẫn
            i = web.chinh_sua_duong_dan(url_first, i)
        if (i not in history) and (i not in url_list):
            if web.kiem_tra_url_da_duyet(i) == True:
                continue
            else:
                url_new.append(i)  ###Thêm đường dẫn hợp lệ vào url_new
    # Lưu lại các url hợp lệ vào url_list
    url_list = url_list + url_new
    # đếm số đường dẫn đã duyệt
    count += 1
    # Lưu lại đường dẫn vừa lấy từ web về vào lịch sử
    folder.luu_lich_su_dulieu_da_cao(url)
    history.append(url)
    # data_array là một list gồm nội dung file html...
    data_array = [content, url_new, url, url_new_limit]
    name_folder = folder.tao_ten_folder()  # Tạo thư mục tự động và kết quả trả về là tên thư mục vừa tạo
    w = folder.luu_file(data_array, name_folder)

    print("Đã duyệt đường dẫn", url)