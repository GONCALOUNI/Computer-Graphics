import numpy as np
from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader

class ModeloGeometry(Geometry):
    def __init__(self):
        super().__init__()
        # Store vertex data
        position_data = my_obj_reader('modelo.obj')
        print("Position Data:", position_data)  # Debugging: Print position_data
        color_data = []
        uv_data = [x for x in position_data]
        # default vertex colors
        c1, c2, c3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
        c4, c5, c6 = [0, 1, 1], [1, 0, 1], [1, 1, 0]
        color_data += [c1, c2, c3, c4, c5, c6]

        self.add_attribute("vec3", "vertexPosition",  position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        #self.count_vertices()
