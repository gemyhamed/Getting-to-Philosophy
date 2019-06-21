from bs4 import BeautifulSoup
import urllib.request

import re
import random

title = "Molecule"

v_list=[]

while True:
    print(title)
    v_list.append(title)
    page="http://www.wikipedia.org/wiki/"+title
    req = urllib.request.Request(page)
    content = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(content, "html.parser")
    article = soup.findAll('h1', {'class':'firstHeading'})[0].contents[0]
    maincontent = soup.findAll("div", { "class" : "mw-parser-output" })[0]
    paragraphs = maincontent.findAll('p')
    x=re.findall(r'\/wiki\/[^"]+', str(paragraphs))
    g=[]
    p=[]
    o=[]
    for y in x:
        y = y.replace('/wiki/', '')
        if y == 'Philosophy':
            title = y
        elif 'Philosoph' in y and y not in v_list:
            g.append(y)
        elif 'logic' in y or 'physics' in y or 'Empiri' in y or 'Religion' in y or 'Socio' in y or 'ology' in y or 'math' in y and y not in v_list:
            p.append(y)
        else:
            o.append(y)
    if title=='Philosophy':
        break
    elif g:
        title = random.choice(g)
    elif p:
        title = random.choice(p)
    else:
        title = random.choice(o)
print(len(v_list))
