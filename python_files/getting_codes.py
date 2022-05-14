from bs4 import BeautifulSoup
import numpy as np
import os
import requests

# Primero vamos a sacar todos los códigos de los países para buscar sobre ellos después

with open('./html_files/countries.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

table = doc.find('table')
countries = table.find_all('tr')

results = {}
file = open('./Datasets/all_codes.csv', 'w')

for i in np.arange(1,len(countries)):
    aux = countries[i].text.split('\n')
    results[aux[1]] = aux[2]
    file.write(str(aux[1]) + ',' + str(aux[2]) + os.linesep)

file.close()


# Ahora vamos a eliminar todos los países que no tengan libros
country_codes = list(results.keys())
pre_url = "https://hammurabi.itam.mx/F/8B3QSUMPNPKN9BTD3CQC14DSHJHEUG634Y2FJVLTYV3AXMYG9Y-32025?ssl_" \
          "flag=Y&func=find-c&local_base=ACERVOITAM&ccl_term=wpl%3D"
post_url = "+and+wft%3Dbk&local_base="

for code in country_codes:
    try:
        url = pre_url + code + post_url
        result = requests.get(url).content
        doc = BeautifulSoup(result, 'html.parser')
        if len(doc.find_all(text=' registros.')) == 0:
            print('Deleted ' + str(code))
            results.pop(code)
    except:
        print(f'Passed {code}')
        pass

# Guardamos los códigos para no estar corriendo esto cada vez
final_codes = list(results.keys())

file = open('./Datasets/final_codes.csv', 'w')
for final_code in final_codes:
    file.write(str(final_code) + ',' + str(results[final_code]) + os.linesep)
file.close()





