from pico2d import*
SCENE_TIME_PER_ACTION = 10
SCENE_PER_TIME = 1.0 / SCENE_TIME_PER_ACTION
import game_framework
class BACKGROUND:
    def get_name(self):
        return 'background'
    def __init__ (self):
        self.image = [load_image("./background/clear/" + "w" + "%d" %i + ".png") for i in range(1, 9)]
        self.bgm = load_music('./music/FinalClear.mp3')
        self.bgm.set_volume(40)
        self.bgm.play()
        self.frame = 0

    def edit_x(self,x):
        self.x-=x
    def get_pos(self):
        return self.x
    def draw (self):
       self.image[int(self.frame)].draw(400,300)

    def update(self):
        self.frame = (self.frame + SCENE_PER_TIME * 8 * game_framework.frame_time) % 8  # 방향 전환 frame: 1

