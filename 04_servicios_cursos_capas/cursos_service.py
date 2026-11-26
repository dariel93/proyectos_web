from pydantic import BaseModel

class Curso(BaseModel):
    codigo:int 
    nombre:str
    tematica:str  
    precio:float
    
class Cursos_service:
    lista_cursos=[]
    
    def alta_curso(self, curso):
        self.lista_cursos.append(curso)
        return curso
    def buscar_tematica(self, tematica):
        return [c for c in self.lista_cursos if c.tematica==tematica]
    def eliminar_curso(self, codigo):
        self.lista_cursos=[c for c in self.lista_cursos if c.codigo!=codigo]
    