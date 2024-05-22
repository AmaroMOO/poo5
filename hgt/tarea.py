class Tarea:
    def __init__(self, tarea:str, id:int, estado:bool) -> None:
       self.tarea = tarea
       self.id = id
       self.estado = estado

    #Metodos CRUD
    def read(self)->str:

        return self.tarea, self.id, self.estado
    
    def update(self, tarea, id, estado)->None:
        self.tarea = tarea
        self.id = id
        self.estado = estado

    def delete(self):
        self.tarea = None
        self.id = None
        self.estado = None