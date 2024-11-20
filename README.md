# Bem-vindo ao nosso Projeto de Banco de Dados!

1. Descrição do projeto
* Este projeto consiste na implementação e construção de um Banco de Dados destinado a uma faculdade ficticia com o objetivo de organizar seus dados, utilizamos neste projeto o banco de dados não relacional (NoSQL) MongoDB, este banco trabalha no formato Document Storage para armazenar os dados, assim, facilitando as queries de buscas realizadas no Banco e otimizando o tempo de processamento das mesmas.

2. Observações
* Utilizamos do Software MongoDB Compass para a criação das bibliotecas de dados e utilizamos o proprio Mongosh para a inserção de dados e realização das queries no Banco.
* Foi adaptado o algoritmo de geração de dados do semestre passado para que ele pudesse gerar dados com base na sintaxe aceita pelo MongoDB.
*  Por conta de ser um banco não relacional, o MongoDB não suporta nenhum tipo de JOINS como em bancos relacionais, porém, existe uma função do proprío Banco chamada "lookup", que permite a realização de buscas em outras bibliotecas de dados, realizar um match de algum atributo em comum e então armazana-la na biblioteca especificada, então utilizamos desta função para facilitar a implementação e agregação dos dados.

3. Como utilizar o código
* Primeiramente é necessario gerar as coleções onde serão armazenados os dados, para isso, basta abrir o [codigo de criação de dados](bancoMongo/gerdadosmong.py) ou o [preset de dados](bancoMongo/dadosInsert.txt) e inserir os dados que o proprio MongoDB ja ira criar as colecoes aqui e inserir o conteudo em cada colecao devidamente.
* As queries que atendem os objetivos propostos podem ser vistas clicando [aqui](bancoMongo/queriesmongo.txt).
* O diagrama das colecoes pode ser visto clicando [aqui](bancoMongo/mongodb.png)

4. Integrantes
* Diego Meira Jardim  R.A: 24.122.094-6
* Lucas Antunes Sampaio  R.A: 24.122.056-5
* Romulo Carneiro de Oliveira Canavesso  R.A: 24.122.093-8
