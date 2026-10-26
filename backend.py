import codepatterns as cpt
import vectors as vt


# Posição, escala, velocidade, aceleração, massa, força, temperatura
class PhysicObject():
    def __init__(self, mass:float=1, heat:float=0, scale:vt.Scale2D|None=None, 
        velo:vt.Velo2D|None=None, accel:vt.Accel2D|None=None):

        self.mass, self.heat = mass, heat
        self.scale, self.velo, self.accel = scale, velo, accel

    def move(self):
        ...