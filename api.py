from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Carro(BaseModel):
    id: int
    modelo: str
    marca: str
    combustivel: str
    cor: str
    ano_veiculo: int

lista = []

@app.post('/cadastrar_carro')
def cadastrar(modelo, marca, combustivel, cor, ano_veiculo):
    id = len(lista) + 1
    carro = Carro(id=id, modelo=modelo, marca=marca, combustivel=combustivel, cor=cor, ano_veiculo=ano_veiculo)
    try:
        lista.append(carro)
        return {'mensagem': 'Carro cadastrado com sucesso'}
    except:
        return {'mensagem': 'Carro não encontrado'}


@app.get('/listar')
def root():
    return {'carros': lista}


@app.post('/atualizar')
def atualizar(carro: Carro):
    for c in lista:
        if c.id == carro.id:
            c.modelo = carro.modelo
            c.marca = carro.marca
            c.combustivel = carro.combustivel
            c.cor = carro.cor
            c.ano_veiculo = carro.ano_veiculo

            return {'mensagem': 'Carro atualizado com sucesso'}
    return {'mensagem': 'Carro não encontrado'}


@app.get('/apagar_carro/{id}')
def apagar_carro(id: int):
    for carro in lista:
        if carro.id == id:
            lista.remove(carro)
            return {'mensagem': 'Carro apagado'}
    return {'mensagem': 'Carro não encontrado'}

