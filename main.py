from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Animal(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    color: str

data_base: List[Animal] = []

#Retornar lista de animais
@app.get('/animais')
def animals_list():
    return data_base

#Retornar um unico animal pelo id
@app.get('/animais/{animal_id}')
def send_animal(animal_id: int):
    for animal in data_base:
        if animal.id == animal_id:
            return animal
    return "Animal não encontrado"

#Deletar registro do animal
@app.delete('/animais/{animal_id}')
def remove_animal(animal_id: int):
    position = -1
    for index, animal in enumerate(data_base):
        if animal.id == animal_id:
            position = index
            break

    if position != -1:
        data_base.pop(position)
        return "Animal removido com sucesso"
    else:
        return "Animal não encontrado"

@app.post('/animais')
def create_animal(animal: Animal):
    data_base.append(animal)
    return "O Animal foi cadastrado com sucesso!"

