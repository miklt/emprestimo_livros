# Aplicação de Empréstimo de Livros em django. Pt 1.
## Objetivo
Apresentar o uso de modelos em django e o mapeamento das classes para um banco de dados relacional (sqlite)

## Definição (simples) do cenário
“Um usuário cadastrado no sistema pode selecionar um livro de uma lista de livros cadastrados e fazer o empréstimo desse livro por uma duração determinada (padrão de 7 dias)”
 
## Instruções
### Pré-requisitos
Para utilizar este repositório você precisa ter python 3.7+ instalado, um editor de texto como o vscode ou pycharm ou acesso a um terminal de linha de comando (linux/mac) ou powershell (windows).

### Passos:
#### 1. Clonar o repositorio
No seu terminal, digite o comando:
``` 
git clone https://github.com/miklt/emprestimo_livros.git
```
####  2. Criar o ambiente virtual 
```
cd emprestimo_livros
python3 -m venv env
```
Para linux ou mac:
```
source env/bin/activate
```
Para windows:
```
.\env\Scripts\Activate.ps1
```
#### 3. Instalar as dependências
```
pip install -r requirements.txt
```
#### 4. Criar a migrações
```
cd projeto
python manage.py makemigrations
```
#### 5. Executar as migrações (criar o banco de dados)
```
python manage.py migrate
```
#### 6. Executar os testes
```
python manage.py test
```

