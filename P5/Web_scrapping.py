import requests as re
from bs4 import BeautifulSoup


FILE = "P5\\article.txt"


def writeText(url):
    html_text = re.get(url).text

    soup = BeautifulSoup(html_text,'lxml')
    #Estrucura donde se encuentra la noticia
    article = soup.find('div', class_='entry-content')
    paragraphs = article.find_all('p')

    with open(FILE,'w',encoding='utf-8') as file:

        for paragraph in paragraphs:
            file.write((paragraph.text + '\n').replace('\n\n','\n'))

    return FILE
