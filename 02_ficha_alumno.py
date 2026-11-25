# Hacer una API REST con una funcion que reciba el DNI del alumno
# y que devuelva su ficha, formada por dni, nombre, edad y email

from pydantic import BaseModel
from fastapi import FastAPI, Response, HTTPException

app = FastAPI()

"""class Alumno:
    def __init__(self, dni, nombre, edad, email):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.email = email"""


"""@app.get("/ficha/{dni}")
def ficha(dni):
    if dni==None:
        return None
    return Alumno(dni, "Dariel Trujillo Chaviano",33,"trujichaviano@gmail.com")"""

class Alumno(BaseModel):
    dni:str 
    nombre:str
    edad:int  
    email:str 

@app.get("/ficha/{dni}", response_model=Alumno)
def ficha(dni)->Alumno:
    if dni==None:
        return None
    return Alumno(dni=dni, nombre="Dariel Trujillo Chaviano", edad=33, email="trujichaviano@gmail.com")

@app.post("/ficha", response_model=Alumno)
def nueva_ficha(ficha:Alumno)->Alumno:
    if len(ficha.dni)<2:
        raise HTTPException(status_code=402, detail="No es posible dar un alta sin dni")
    print(ficha.nombre)
    return ficha

@app.delete("/ficha/{dni}")
def eliminar_ficha(dni, resp:Response):
    if len(dni)<2:
        resp.status_code=409
        return
    resp.status_code=200
    print(f"Eliminando ficha: {dni}")