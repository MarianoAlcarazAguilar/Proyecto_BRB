import os
import pandas as pd

data = pd.read_csv('./Datasets/final_codes.csv')
codes = list(data.code)
countries = list(data.country_name)

file = open('final_urls.txt', 'w')

pre_url = "https://hammurabi.itam.mx/F/8B3QSUMPNPKN9BTD3CQC14DSHJHEUG634Y2FJVLTYV3AXMYG9Y-32025?ssl_" \
          "flag=Y&func=find-c&local_base=ACERVOITAM&ccl_term=wpl%3D"
post_url = "+and+wft%3Dbk&local_base="

for code in codes:
    url = pre_url + code + post_url
    file.write(str(url) + os.linesep)

file.close()
