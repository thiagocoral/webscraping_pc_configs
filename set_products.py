from web_scrap_kabum import get_product
import json
import os

urls = ["https://www.kabum.com.br/produto/129459/processador-amd-ryzen-7-5800x-cache-36mb-3-8ghz-4-7ghz-max-turbo-am4-100-100000063wof","https://www.kabum.com.br/produto/167209/placa-de-v-deo-gigabyte-aorus-radeon-rx-6700-xt-elite-12g-rgb-gddr6-dlss-ray-tracing-gv-r67xtaorus-e-12gd","https://www.kabum.com.br/produto/155123/placa-de-v-deo-msi-radeon-rx-6700-xt-mech-2x-12g-oc-16-gbps-12gb-gddr6-dual-fan-912-v398-002","https://www.kabum.com.br/produto/153200/placa-m-e-gigabyte-b560m-aorus-elite-rev-1-0-lga1200-micro-atx-ddr4"]
dic_prods = {1:["https://www.kabum.com.br/produto/167209/placa-de-v-deo-gigabyte-aorus-radeon-rx-6700-xt-elite-12g-rgb-gddr6-dlss-ray-tracing-gv-r67xtaorus-e-12gd"]}


def add_product_url(url):
    if os.path.isfile("urls.txt"):
        open("urls.txt","w",encoding='utf-8')
        print("file urls.txt created")
        with open("urls.txt","a") as url_file:
            text_urlfile = url + "\n"
            url_file.write(text_urlfile)



def insert_product(url):
    if not os.path.isfile("products.json"):
        start_data = {
            "products": []
        }
        with open("products.json","w",encoding='utf-8') as file:
            json.dump(start_data,file)
        print("file products.json created")

    def add_product(new_product):
        with open("products.json","r+", encoding='utf-8') as file:
            full_file = json.load(file)
            id = len(full_file["products"]) + 1
            new_product["ID"]=id
            full_file["products"].append(new_product)
            file.seek(0)
            json.dump(full_file, file, indent = 4, ensure_ascii=False)

    product = get_product.get_data(urls[0])

    add_product(product)

def read_urls():
    with open("urls.txt","r") as url_file:
        lines = url_file.readlines()
        for line in lines:
            if len(line)>10:
                insert_product(line)

read_urls()