import nltk

try:
    nltk.dowload('punkt')
    print(" NLTK punkt descargado correctamente")
except Exception as e:
    print("Error durente la descarga:",e)
