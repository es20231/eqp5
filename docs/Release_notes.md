# PostBook 1.0

O PostBook é uma aplicação web que funciona como uma rede social
com interação de postagens entre usuários.

# 1. Features disponíveis para esta versão:

* Login de usuário
* Logout de usuário
* Recuperação de senha através de e-mail
* Cadastro de novo usuário
* Tela inicial
* Upload de fotos
* Editar perfil
* Mudar senha
* _Like_ e _deslike_
* Gerenciar comentários
* Realizar _uploads_ múltiplos
* Realizar filtros de imagem

# 2. Tecnologias, bibliotecas e framework desta versão:

* Python
* Django
* Rest Framework
* Cors-headers
* DotEnv
* Pillow
* Pytest
* Vue.js
* Babel.js
* JavaScript
* Jest
* Selenium WebDriver

# 3. Download, configuração, instalação e execução:

* É preciso ter o Python instalado
* É preciso ter o Django instalado
* É preciso ter o MySQL instalado
* É preciso ter pip do Python instalado

Instalando as dependências usando o comando
```
pip install -r requirements.txt
```
Migrando o dados para o database usando o comando
```
python manage.py migrate
```
e
```
python manage.py makemigration
```

# Execução da aplicação:

Back-end
```
python manage.py runserver
```

Front-end
```
npm run serve
```

# 4. Casos de testes e resultados de testes:

[Casos de testes](https://github.com/es20231/eqp5/blob/gleideson_freitas/docs/test/teste.md)

[Resultados dos testes](https://github.com/es20231/eqp5/blob/gleideson_freitas/docs/test/resultados_testes_prototipo1%20-%20P%C3%A1gina1.csv)

# 5. Execução de testes unitários/integração:

Back-end
```
python manage.py tests
```
Front-end
```
npm run test:unit
```
O _Selenium WebDriver_ é executado como um script comum usando o node.js:
```
node system/**/**.js
```
