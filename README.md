# api_teste
criando uma API com o framework python Flask

## passo a passo

1. crie um ambiente viertual python para sua maquina:
```bash
    $ python3 -m venv venv
```
2. instale o flask na sua máquina:
```bash
    $ pip install flask
```
3. basico de flask:
```python
# realizar a importação do flask
from flask import Flask

# instanciar a class Flask
app = Flask(__name__)

# iniciar o servidor 
app.run()
```

toda a sua logica da api deve ser escrita entre sua instaciação e a função de inicialização do servidor **app.run()**. 

para criar uma rota devemos usar o decorator:
```python
@app.route(<rota>, <methods>)
def funcao():
    return make_response( # construir uma resposta para a api
        jsonify(dado) # transformar os dados em um json para ser enviado
    )
```

**endpoint**: seria uma rota definida;