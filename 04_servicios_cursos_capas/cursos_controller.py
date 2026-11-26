"""API REST para cursos
Un curso se identifica por codigo,nombre,tematica y precio
Expondrá los siguientes recursos:

-Alta de curso. Se recibe un curso y lo da de alta
Devuelve el curso curso añadido
-Buscar cursos por tematica. Se recibe una temática
y devuelve todos los cursos de esa temática
-Eliminar curso. Se recibe un código de curso, y se elimina
Si el código no es válido(<0) se genera error 409 """

from fastapi import FastAPI, Response, HTTPException
from typing import List
from cursos_service import Curso, Cursos_service

app = FastAPI()
service = Cursos_service()
@app.post("/curso", response_model=Curso)
def alta_curso(curso:Curso):
    return service.alta_curso(curso)

@app.get("/cursos", response_model=List[Curso])
def cursos_tematica(tematica:str):
    return service.buscar_tematica(tematica)

@app.delete("/curso")
def eliminar_curso(codigo:int):
    if codigo<=0:
        raise HTTPException(status_code=409, detail="Código de curso inválido!")
    service.eliminar_curso(codigo)