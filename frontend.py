import codepatterns as cpt
import pygame as pg
import vectors as vt

class Camera(metaclass=cpt.SingletonMeta):
    def __init__(self, pos_xy: vt.Pos2D, pos_z:float):
        self.pos_xy = pos_xy
        self.pos_z = pos_z
    
    def move(self, velo_xy:vt.Velo2D, velo_z:float):
        self.pos_xy += velo_xy
        self.pos_z += velo_z

# Classe 'GameObject' para adaptar o sistema
class GameAdapter(cpt.Adapter):
    
    class GameObject():
        def __init__(self, physicObject):
            self.color = physicObject.color
            self.scale = physicObject.scale
            self.pos = physicObject.pos - self.scale/2

    def __init__(self, adaptee:list):
        super().__init__(adaptee)

    def adapt(self) -> list[GameObject]:
        return [self.GameObject(phy_obj) for phy_obj in self._adaptee]

class Window(metaclass=cpt.SingletonMeta):
    def __init__(self, game_objs:list[GameAdapter.GameObject], scale:vt.Scale2D):
        self.game_objs = game_objs
        self.scale = scale

        pg.init()
        self.screen = pg.display.set_mode(scale.xy)
        self.clock = pg.time.Clock()

    def run(self):
        on_running = True
        while on_running:

            for event in pg.event.get():
                if event.type == pg.QUIT: on_running = False

            self.screen.fill('#ffffff')



            pg.display.flip()
            self.clock.tick(60)
        pg.quit()

if __name__ == "__main__":
    window = Window(vt.Scale2D(1000,800))
    window.run()