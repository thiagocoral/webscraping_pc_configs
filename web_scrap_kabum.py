#!/usr/bin/env python
# coding: utf-8

# In[12]:


from bs4 import BeautifulSoup
import requests



class get_product:
    def __init__(self,url):
        self.url = url

    def get_data(url):
        page = requests.get(url)
        web_scraped = BeautifulSoup(page.text,"html.parser")
        title_prod = web_scraped.title.text
        article = web_scraped.find_all("article")
        preco = article[0].find_all("h4")[0].text
        preco_prod = preco[0 : 2 : ] + preco[2 + 1 : :]

        tech_info = web_scraped.find(id="secaoInformacoesTecnicas")
        specs = ""
        for p in tech_info.find_all("p"):
            specs += p.text
        ps = tech_info.find_all("p")
        brand = ps[1].text.split(": ")[1]
        model = ps[2].text.split(": ")[1]

        kind = None
        title_splited = title_prod.split(" ")
        if title_splited[0].upper() == "PROCESSADOR":
            kind = "Processador"
        elif title_splited[0].upper() == "GABINETE":
            kind = "Gabinete"
        elif title_splited[0].upper() == "SSD":
            kind = "SSD"
        elif title_splited[0].upper() == "MEMÓRIA":
            kind = "Memória"
        elif title_splited[0].upper() == "PLACA":
            if  title_splited[2].upper() == "VÍDEO":
                kind = "Placa de Vídeo"
            elif title_splited[1].upper() == "MÃE":
                kind = "Placa Mãe"


        product = {"kind":kind,"modelo":model,"brand":brand,"preco":preco_prod,"title":title_prod,"url":url,"specs":specs}

        return product


