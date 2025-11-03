from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()

boxes = []
for i in range(40):
    for j in range(40):
        box = Button(color=color.white, model='cube',position=(j,0,i),
                    texture='grass.jpg',parent=scene,origin_y = 0.5)
        boxes.append(box)

def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'e':
                new = Button(color=color.white, model='cube',position=box.position + mouse.normal,
                    texture='wood.jpg',parent=scene,origin_y = 0.5)
                boxes.append(new)
            if key == 'q':
                boxes.remove(box)
                destroy(box)

app.run()