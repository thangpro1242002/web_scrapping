import web_url
import luu_url

def start():
    url_list = ['https://vietnamnet.vn/']
    history = []  # DS các đường dẫn đã duyệt
    max_page = 15  # quy định số lượng trang web được tải về
    count = 0  # đếm số lượng trang web đã tải về
    data_folder = "C:\\webscrapping\\"
    # Tạo Folder
    folder.tao_thu_muc(data_folder)
    # kịch bản tải các trang web
    while (count < max_page) and (len(url_list) > 0):
        url = url_list.pop(0)
        # Đọc nội dung
        page = web_url.doc_noi_dung(url)
        # Lấy tất cả đường dẫn
        links = web_url.lay_duong_dan((page))
        for item in links:
            if not web_url.kiem_tra_duong_dan(item):
                item = web_url.chinh_sua_duong_dan("https://vietnamnet.vn/", item)
            if not ((item in url_list) and (item in history)):
                url_list.append(item)
        luu_url.luu_noi_dung(page, data_folder, count)
        history.append(url)
        # đếm số đường dẫn đã duyệt
        count += 1
      
    if __name__ == '__main__':
    start()
