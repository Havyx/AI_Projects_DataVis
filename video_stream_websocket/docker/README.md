## DOCKERFILE
https://codefresh.io/docker-tutorial/hello-whale-getting-started-docker-flask/
https://medium.com/@doedotdev/docker-flask-a-simple-tutorial-bbcb2f4110b5
-----------------------------------------------------------------------------------------------------
Criar uma pasta pra cada container. ex: pasta web 
  
`` mkdir web ``
`` cd web ``  
  
Copie a aplicação para a pasta: 
`` cp ../app.py . ``  
  
Crie uma Dockerfile e o arquivo requirements.txt
``touch Dockerfile``
``touch requirements.txt``  
  
Na dockerfile: "PULL PYTHON UBUNTU FROM DOCK HUB" (Instruções de como construir a maquina)
``FROM python:3``
``WORKDIR /usr/src/app``  
  
Diz a maquina que esse sera o diretorio de trabalho dentro dessa maquina.  
  
``COPY requirements.txt . `` 
Copia requirements da pasta WEB para o direto de trabalho da maquina.   "Nao esquecer o ponto"
  
Agora instale as dependecias na maquina
``RUN pip install --no-cache-dir -r requirements.txt
  
Para finalizar copia o app.py e requirements.tzt da pasta web para o diretorio de trabalho da máquina   
`` COPY . . ``  
  
Entao rode o comando de inicialização da maquina  
``CMD ["python", "app.py"]
---------------------------------------------------------------------------------------------------
Na pasta raiz cd ../ podemos ter outras pastas dockers ex web, db... Precisamos aqui um orquestrator para dizer como esses dockers se comunicam entre si.  
``touch docker-compose.yml``  

Agora começamos a escrever no arquivo:  

``version: '3'  
  
Quais são os serviços?  

``
services:  
  web:  
    build: ./web  
    ports:
      - "5000:5000"  
  db:
    build: ./db
``
  
Para construir os containers:
  
``docker-compose build``  

Para rodar os containners:  
docker-compose up