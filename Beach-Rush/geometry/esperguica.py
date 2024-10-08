from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader


class espreguicaGeometry(Geometry):
    def __init__(self):  # Por padrão, estamos configurando a cor para branco
        super().__init__()

        vertices, texture = my_obj_reader('objetos/1.obj')


        self.add_attribute("vec3", "vertexPosition", vertices)
        self.add_attribute("vec2", "vertexUV", texture)