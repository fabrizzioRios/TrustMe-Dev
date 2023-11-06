import whois
import requests

url_page = 'https://campus.uag.mx/SSO'


def validate_pages(url_page):
    try:
        page_state = requests.get(url_page).status_code
        if page_state == 200:
            page_info = whois.whois(url_page)
            print(page_info)
        else:
            print(page_state)
    except:
        print("No se encontró la página")


validate_pages(url_page)
