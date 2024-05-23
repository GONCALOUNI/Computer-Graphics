from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader


class ModeloPulGeometry(Geometry):
    def __init__(self):
        super().__init__()

        # Carregar vértices do arquivo .obj
        vertices, texture = my_obj_reader('objetos/modelopul.obj')


        self.add_attribute("vec3", "vertexPosition", vertices)
        self.add_attribute("vec2", "vertexUV", texture)
