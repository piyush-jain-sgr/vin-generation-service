import re
#1HGPJ72XXVF986395
input="1HGPJ72X1VF986398"
print(re.search("^[1-9]{1}[A-Za-z]{4}[0-9]{2}[A-Za-z]{4}[0-9]{6}$", input))
