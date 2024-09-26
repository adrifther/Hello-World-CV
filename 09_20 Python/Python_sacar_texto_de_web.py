import requests
from bs4 import BeautifulSoup
import re

patro = re.compile("(?<!\S)[0-9]{4}(?!\S)")


# URL de la página de Wikipedia que quieres obtener
url = "https://es.wikipedia.org/wiki/Python_(lenguaje_de_programación)"

# Realiza la petición a la página
response = requests.get(url)

# Comprobar que la petición fue exitosa (código 200)
if response.status_code == 200:
# Crear el objeto BeautifulSoup para parsear el HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar el contenido principal de la página
    content = soup.find(id="mw-content-text")

    # Extraer todo el texto del contenido
    texto = content.get_text()
    resultat=patro.findall(texto)
    print(resultat)
else:
    print("No se pudo acceder a la página.")