from bs4 import BeautifulSoup
from mdutils.mdutils import MdUtils
import requests


# get the words list
text_file = open(".\words.txt", "r")
#read whole file to a string
data = text_file.read()
#close file
text_file.close()

words = [x.strip() for x in data.split(",")]

url = 'https://dictionary.cambridge.org/dictionary/english/'

headers = {'user-agent': 'my-app/0.0.1'}

mdFile = MdUtils(file_name='Example_Markdown',title='Markdown File Example')

mdFile.new_header(level=1, title='Describe actions as bad')

mdFile.new_header(level=2, title='Actions')
    
for word in words:
    mdFile.new_header(level=3, title=word)
    
    u = url + word
    r = requests.get(u, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # def-block ddef_block ( mulitple instances )
    blocks = soup.find_all("div", class_="def-block ddef_block")

    print(len(blocks))

    for b in blocks:
        title = b.find("div", class_="ddef_h").get_text().strip()
        # ddef_h (single instance )
        mdFile.new_paragraph(title)
        # examp dexamp ( multiple instances )
        examples = b.find_all("div", class_="examp dexamp")
        ex = [ex.get_text().strip() for ex in examples]
        mdFile.new_list(ex)
    

mdFile.create_md_file()