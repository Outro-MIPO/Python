from googletrans import Translator

translater = Translator()
Be_The_Best=''' 
Transport
'''
out=translater.translate(Be_The_Best,dest="fr")

print(out.text)
