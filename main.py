import web_url
import luu_url

def main():
    url_goc=input("Nhập link khởi đầu:")
    url_goc = input('Nhập link khởi đầu: ')
    url_goc = web_url.sua_url_goc(url_goc)
    url_tim_duoc = web_url.tim_url_lien_quan(url_goc, url_goc)
    waiting_line = url_tim_duoc
    history = web_url.them_va_duyet_hang_cho(waiting_line, url_goc)
    luu_url.tao_thu_muc('bong_da_2')
    luu_url.luu_tat_ca_file(history)
    

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
