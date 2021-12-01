import requests
from bs4 import BeautifulSoup


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")


def sitioweb():
    soup = get_soup("https://ligamx.net/cancha/tablas/tablaGeneralClasificacion/sp/4c808cb74d7b45")
    rows = soup.find_all("table")[0].find_all("tr")
    archivo = open("resultados_webscraping.txt", "w")
    for row in rows:
        columns = row.find_all("td")
        archivo.write('columns= % s' %columns)
        t = [ele.text.strip() for ele in columns]
#       print(f"{t}") 

    archivo.close() 

if __name__ == "__main__":
	sitioweb()
