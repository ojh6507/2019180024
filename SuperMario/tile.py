from pico2d import*

round1 =[ 
    [0 for n in range(16)],
    [0 for n in range(16)],
    [0 for n in range(16)],
    [1 for n in range(16)],
    [2 for n in range(16)]
]
class BACKGROUND:
    def get_name(self):
        return 'background'
    def __init__ (self):
        self.image = load_image('background_2.png')
        self.x = 3750
    def draw (self):
        self.image.draw(self.x, 500)

    def update(self):
        pass
