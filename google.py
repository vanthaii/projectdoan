import googletrans
from googletrans import Translator
t=Translator()
a=t.translate("em dep qua",src="vi",dest="en")
print(a.text)