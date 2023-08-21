import json
from googletrans import Translator,LANGUAGES


#print(LANGUAGES)
gt=Translator()
#r=gt.translate('hello','fa','en')
#print(r.text)


with open('en.json',encoding='utf-8') as json_data:
    data=json.load(json_data)

#print(data['RegistrationForm_Fullname'])
for d in data:
    print(data[d])
    r=gt.translate(data[d],'nl','en')
    data[d]=r.text
    print(r.text)


f = open("du.json", "w",encoding='utf-8')

f.write(str(data).replace("'",'"'))
f.close()




