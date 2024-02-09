# Python Google Sheets API Application

Aplicação em Python que se conecta à Google Sheets API para manipular os dados de uma planilha, com o objetivo de calcular o desempenho de nota e falta dos alunos para aprovação ou reprovação.

Essa aplicação foi realizada com o objetivo de participar de um teste prático.

## Pré-requisitos

Antes de começar, certifique-se de que você tenha feito o seguinte:

- Criou um projeto no [Google Cloud Console](https://console.cloud.google.com/).
- Habilitou a Google Sheets API para o seu projeto.
- Criou as credenciais de serviço e baixou o arquivo JSON com essas credenciais.

Informações detalhadas sobre os passos acima podem ser encontradas no [Guia de início rápido do Python](https://developers.google.com/sheets/api/quickstart/python?hl=pt-br).

## Configuração

1. Coloque o arquivo JSON com as suas credenciais na pasta raiz do projeto.
2. Renomeie o arquivo JSON para `credentials.json`.

Obs.: os pré-requisitos e configurações só serão necessários se não for utilizar as credenciais e planilha de exemplo.

## Instalação

1. Instale os pacotes usando o comando:

```
pip install -r requirements.txt
```

## Uso

Execute no terminal o comando `python main.py` para iniciar a aplicação. 

A aplicação está configurada para acessar uma [planilha de exemplo](https://docs.google.com/spreadsheets/d/1eFTeFhnTtIFhEigmd5R3g-cJiYkHbNpsA0N4M5y-fO4/edit#gid=0), bem como já existe uma credencial disponível na pasta `api` para que possa realizar os testes, mas você pode modificar o código para atender às suas necessidades específicas.

Caso seja o primeiro acesso, será solicitada uma autorização no navegador, a qual deverá ser dada para que se possa utilizar a aplicação. Após essa autorização, será gerado um arquivo `token.json` na pasta `api`. Com esse arquivo, não será mais necessário dar autorização, pois a aplicação já estará logada na sua conta.

## Funcionalidades

- Ler dados de uma planilha.
- Escrever dados em uma planilha.
- Atualizar dados em uma planilha.

## Contribuindo

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request se desejar contribuir para este projeto.
