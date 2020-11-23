from dotenv import load_dotenv
import json
from tweepy import OAuthHandler, Stream, StreamListener # Faz requisições para API do Twitter 
import os
from datetime import datetime


# Get Twitter Developer Keys
load_dotenv()
API_KEY = os.getenv('API_KEY') # Consumer Key
API_SECRET_KEY = os.getenv('API_SECRET_KEY') # Consumer Secret
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


# Definir um arquivo de saída para armazenar os tweets coletados
today = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
out = open(f'collected_tweets_{today}.txt', 'w') # W - para abrir em modo de escrita

# Definição de classe para conexão com o Twitter
class MyListener(StreamListener):
    
    def on_data(self, data):
        # Informa ao python que os dados estão em json
        itemString = json.dumps(data)
        # Salva cada tweet em uma nova linha
        out.write(itemString + "\n")
        return True

    def on_error(self, status):
        print(status)       


# Implementação da função main
if __name__ == "__main__":
    listener = MyListener()
    
    # Autenticação de chaves
    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Instancia da classe que realiza-ra o streaming de dados
    stream = Stream(auth, listener)

    # Filter da API do Twitter onde setamos as palavras-chaves que será monitorada
    stream.filter(track=["Trump"])
 
