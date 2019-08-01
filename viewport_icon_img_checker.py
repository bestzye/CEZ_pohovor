#!/usr/bin/env python
# coding: utf-8

# In[116]:


import requests
import re


# In[138]:


with open ('C:\\Users\\katerina.vobecka\\Desktop\\zkusebni_url.txt') as words:
    content = words.readlines()
    content = [x.strip() for x in content]


# In[174]:


for a in content:
    f = re.split(r',', a)
    f = ["http://" + fs for fs in f]
    f = ('.'.join(f[::-1]))
    response = requests.get(f)
    html = response.text
    pocet_src = html.count('img src="')
    pocet_id = html.count('img id="')
    pocet_class = html.count('img class="')
    pocet_obrazky = pocet_id + pocet_src + pocet_class
    if '<meta name="viewport" content="' in html:
        if 'link rel="shortcut icon"' in html or 'rel="apple-touch-icon"' in html or 'link rel="icon"' in html:
            print(f + ' (Has Viewport), '  + ' (Has Icon), '+ '(pocet_obrazku: ', pocet_obrazky,')')
        else:
            print(f + ' (Has Viewport), '  + ' (No Icon), '+ '(pocet_obrazku: ', pocet_obrazky, ')')
    else:
        if 'link rel="shortcut icon"' in html or 'rel="apple-touch-icon"' in html or 'link rel="icon"' in html:
            print(f + ' (No Viewport), '  + ' (Has Icon), ' + '(pocet_obrazku: ', pocet_obrazky, ')')
        else:
            print(f + ' (No Viewport), '  + ' (No Icon), ' + '(pocet_obrazku: ', pocet_obrazky, ')')


# In[ ]:




