from sys import stdin
input = stdin.readline
import re
  
html_doc = input().strip() 
  
html_doc = html_doc[len('<main>'): -len('</main>')]  
  
html_doc = re.sub(r'<div +title="([\w ]*)">', r'title : \1\n', html_doc)  
html_doc = re.sub(r'</div>', '', html_doc)  
  
html_doc = re.sub(r'<p>', '', html_doc)  
html_doc = re.sub(r'</p>', '\n', html_doc)  
  
html_doc = re.sub(r'</?[\w ]*>', '', html_doc)  
html_doc = re.sub(r' ?\n ?', '\n', html_doc)  
html_doc = re.sub(r' {2,}', ' ', html_doc)  
  
print(html_doc)