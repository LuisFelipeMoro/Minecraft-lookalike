from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
engine = Ursina()

block_pick = 1

def update():

    global block_pick

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    block.Selected()

class   Selected_block(Entity):

    def __init__(self, texture = 'grass_block'):
        super().__init__(
            parent=camera.ui,
            model='block',
            scale=0.05,
            color = color.white,
            texture='assets/grass_block',
            rotation=Vec3(0, -20, -8),
            position=Vec2(0.75, 0.40),
        )
    def Selected(self):
        if block_pick == 1: self.texture = 'grass_block'
        if block_pick == 2: self.texture = 'dirt_block'
        if block_pick == 3: self.texture = 'stone_block'
        if block_pick == 4: self.texture = 'brick_block'

class Voxel(Button):

    def __init__(self, position = (0,0,0), texture = 'grass_block'):
        super().__init__(
            parent = scene,
            position = position,
            model = 'block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5
        )
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture= 'grass_block')
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture='dirt_block')
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture='stone_block')
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture='brick_block')
            if key == 'left mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            color = color.white,
            scale = 150,
            texture = 'Assets/skybox',
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'arm',
            scale = 0.2,
            texture = 'assets/arm_texture',
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6),
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))
        voxel = Voxel(position=(x,-1,z), texture = 'dirt_block')


player = FirstPersonController()
sky = Sky()
hand = Hand()
block = Selected_block()

engine.run()



