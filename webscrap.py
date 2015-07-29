from lxml import html
import requests
page = requests.get('http://127.0.0.1/fb.html')
print page
tree = html.fromstring(page.text)
q = tree.xpath('//class[@data-inset="_5xhk"]/text()')
print(q)
