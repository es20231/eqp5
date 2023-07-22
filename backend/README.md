# BackEnd

## Criar o ambiente virtual
```
virtualenv venv 
```

## Ativar o ambiente virtual
```
.venv/bin/activate (Linux) ou .venv\Scripts\activate(Windows)
```

## Instalando as dependências
```
pip install -r requirements.txt
```

## Criando e rodando as migrações
```
python manage.py makemigrations
```

## Aplicando as migrações
```
python manage.py migrate
```

## Rodar o servidor localmente
```
python manage.py runserver
```

### Personalizar configuração
Consulte [Referência de Configuração](https://docs.djangoproject.com/en/4.1/topics/settings/).