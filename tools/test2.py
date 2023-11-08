import json
import whois
import requests
from datetime import datetime, timedelta

url_page = 'https://campus.uag.mx/SSO'

with open('test.json', 'r') as archivo:
    datos_json = json.load(archivo)


def Whois_tool(url_page):
    try:
        page_state = requests.get(url_page).status_code
        if page_state == 200:
            whois_info = whois.whois(url_page)
        else:
            print("Status:", page_state)
    except:
        print("No se encontró la página")

    return whois_info


def trustme_info(url_page, datos):
    for item in datos:
        pages = item.get('pages', [])
        for page in pages:
            if page.get('url', '') == url_page:
                return page


def pag_validate(url_page, datos):
    info_whois = Whois_tool(url_page)
    trust_page = trustme_info(url_page, datos)
    if info_whois.tech_state == trust_page.get('tech_state'):
        if info_whois.tech_city == trust_page.get('tech_city'):
            if info_whois.tech_country == trust_page.get('tech_country'):
                if info_whois.tech_name == trust_page.get('tech_name'):
                    current_date = datetime.now()
                    time_difference = current_date - info_whois.creation_date
                    if time_difference > timedelta(days=30):
                        print("Cambiar a estatus Válido")
                    else:
                        print("Suspicious Date")
                else:
                    print("Name Fail")
            else:
                print("Country Fail")
        else:
            print("City Fail")
    else:
        print("State Fail")


pag_validate(url_page, datos_json)
