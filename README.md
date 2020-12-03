
![IGTI logo](https://github.com/diegorech/twitter_crawler/blob/main/assets/igtilogo.jpg)
# IGTI Data Engineer Bootcamp 

# Twitter Crawler

Projeto consiste em um crawler para o Twitter que armazena tweets que possuem uma determinada palavra-chave.
Um .json com os tweets capturador é gerado em sua pasta raíz e ao final o dado passa por um tratamento e é inserido em uma tabela no SQLServer seguindo o schema a baixo:

![schema final pós tratamento](https://github.com/diegorech/twitter_crawler/blob/main/assets/Sem%20t%C3%ADtulo.png)

*Para rodar o crawler você precisa de uma [conta de desenvolvedor do twitter.](https://developer.twitter.com/en/apply-for-access)*

### Scripts

`get_tweet.py` - Ao ser executado cria uma conexão com a API do Twitter, captura tweets seguindo uma lista de palavras-chave e os armazena em um .json na diretório atual.

> A lista de palavras-chaves é setada no método `filter()` da class `Stream`
```
  # Instancia da classe que realiza-ra o streaming de dados
    stream = Stream(auth, listener)

    # Filter da API do Twitter onde setamos as palavras-chaves que será monitorada
    stream.filter(track=["COVID", "Corona", "corona vírus"])
```

Enquanto não for encerrado manualmente, `get_tweet.py` **continua capturando e armazenando tweets.**


##### Aconselho encerrar o processo `get_tweets.py` antes de iniciar `analyze.ipynb`.



`analyze.ipynb` - O workflow do notebook segue a ordem a baixo:
  1. Gera um Pandas DataFrame a partir dos tweets capturados em `collected_tweets_{today}.txt`.
  2. realiza a limpeza do dataset excluindo colunas desnecessárias ou que estejam aninhadas. 
  3. Cria de novas colunas a partir do tratamento de colunas existentes. 
  4. Remove valores `null`.
  5. Cria conexão com banco de dados SQLServer.
  6. Insere os dados em uma tabela relacional.

