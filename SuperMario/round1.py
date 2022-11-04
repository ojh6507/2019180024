from pico2d import*

class BACKGROUND:
    def __init__ (self):
        self.image = load_image('background_2.png')
        self.x = 3750
    def draw (self):
        self.image.draw(self.x, 500)

    def update(self):
        pass
        # global player
        # if self.background_x < (-2950):
        #     if player.x - 400 < 0:
        #         self.background_x -= (player.x - 400)
        #         player.x = 400
        #
        # elif player.x - 400 > 0:
        #     self.background_x -= (player.x - 400)
        #     player.x = 400
        #
        # elif player.x - 400 < 0:
        #     if self.background_x - (player.x - 400) < 3750:
        #         self.background_x -= (player.x - 400)
        #         player.x = 400

