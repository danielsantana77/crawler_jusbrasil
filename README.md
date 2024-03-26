## Desafio Jusbrasil - Crawler de tribunais

Esse projeto tem como objetivo o desenvolvimento de uma API para realizar buscas de dados sobre processos nos tribunais de Alagoas e Ceará (1º e 2º grau )

Através do **CNJ**, os seguintes dados dos processos serão coletados :

- classe
- área
- assunto
- data de distribuição
- juiz
- valor da ação
- partes envolvidas no processo
- lista de movimentações

Tribunais que serão consultados:

- TJAL
  - 1º grau - https://www2.tjal.jus.br/cpopg/open.do
  - 2º grau - https://www2.tjal.jus.br/cposg5/open.do
- TJCE
  - 1º grau - https://esaj.tjce.jus.br/cpopg/open.do
  - 2º grau - https://esaj.tjce.jus.br/cposg5/open.do 

## 🔧 Instalação 

Clone o repositorio, através de uma IDE ou via Terminal
  - git clone - https://github.com/danielsantana77/crawler_jusbrasil.git

### 🐳 Via Docker

Para rodar o projeto localmente, siga os seguintes passos:

No terminal:
-  rode o comando 
```
docker build -t crawler_jusbrasil . 
```
-  rode o comando 
```
docker run -d -p 5000:5000 crawler_jusbrasil
```


### 🏠 Localmente

No terminal:

- rode o comando `pip install -r requirements.txt`
- execute o arquivo `app.py`


## 💻 API

Para ter acesso aos dados buscados pela API é preciso:

- `POST` - realizar uma requisição POST para a seguinte rota 
  - http://127.0.0.1:5000/api/collect
  - Passando no body da requisição o **JSON** no formato {"processo" : "CNJ"}
  - Exemplo : {"processo" : "0710802-55.2018.8.02.0001"} ou {"processo" : "07108025520188020001}

## 💻 Tecnologias

- Linguagem :
  - Python
- Bibliotecas :
  - Requests
  - BeautifulSoap
- Framework : 
  - Flask
- Testes :
  - Pytest 