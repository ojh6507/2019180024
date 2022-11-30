from pico2d import *
import random
import game_framework
import game_world
import server
import stage_clear
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 25.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

JUMP_SPEED_KMPH = 10.0
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)


class BOSS:
    images = None
    font = None
    def __init__(self):
        if BOSS.images ==None:
            BOSS.images = {}
            BOSS.images['walk'] = [load_image("./monster/walk/" + "b_walk" + "%d" %i + ".png") for i in range(1, 20)]
            BOSS.images['dead'] = [load_image("./monster/etc/" + "die.png")for i in range(1, 20)]
            BOSS.images['fall'] = [load_image("./monster/etc/" + "fall.png") for i in range(1, 20)]
            BOSS.images['defense'] = [load_image("./monster/etc/" + "defense.png") for i in range(1, 20)]
            BOSS.images['stand'] = [load_image("./monster/etc/" + "stand.png") for i in range(1, 20)]
            BOSS.images['chance'] = [load_image("./monster/etc/" + "chance.png") for i in range(1, 20)]

        if BOSS.font == None:
            BOSS.font = load_font('ENCR10B.TTF', 20)

        self.Y_gravity = 0.25
        self.pre_velocity = 0
        self.y_velocity = 0
        self.jump_height = 0

        self.frame = 0
        self.x = 600
        self.y = 100
        self.dir = 1
        self.action = 1
        self.clip = 17
        self.reflect = 'h'
        self.speed = 0
        self.timer = 1.2
        self.timer_1 = 4.0
        self.timer_2 = 1.5
        self.defense = False
        self.hard = False
        self.build_behavior_tree()
        self.hp = 100
        self.x_size = 70
        self.y_size = 70
        self.chance = False
    def update(self):
        self.hp = clamp(0, self.hp, 100)
        if (not self.defense or self.hard) and not self.chance and self.hp > 0:
            self.bt.run()
            self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        # self.x = clamp(20, self.x, 780)
        self.y = clamp(70,self.y,90)
        self.pre_velocity = self.y_velocity
        self.y += self.y_velocity * JUMP_SPEED_PPS * game_framework.frame_time
        self.y_velocity -= self.Y_gravity
        self.frame = (self.frame + ACTION_PER_TIME * self.clip * game_framework.frame_time) % self.clip  # 방향 전환 frame: 1

        if self.hard:
            self.timer = 4
            self.speed = RUN_SPEED_PPS

        if self.defense:
            self.timer -= game_framework.frame_time
            if self.timer <= 0:
                self.defense = False
                self.timer = 1.2

        if self.hard:
            self.timer_1 -= game_framework.frame_time
            if self.timer_1 <= 0:
                self.chance = True
                self.y+= 5
                self.hard = False

        if self.chance:
            self.timer = -1
            self.timer_2 -= game_framework.frame_time
            if self.timer_2 <= 0:
                self.hard = False
                self.chance = False
                self.timer_2 = 1.5
                self.timer_1 = 4.0
                self.speed = RUN_SPEED_PPS


    def find_player(self):
        distance2 = (server.player.x - self.x) ** 2
        if distance2 <= (PIXEL_PER_METER * 20) ** 2:
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        self.dir = math.atan2( 0, server.player.x - self.x)
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        find_player_node = LeafNode('Find Player', self.find_player)
        move_to_Player_node = LeafNode('Move to Player', self.move_to_player)
        chase_node = SequenceNode('Chase')
        chase_node.add_children(find_player_node, move_to_Player_node)
        self.bt = BehaviorTree(chase_node)

    def draw(self):
        if self.defense:
            if self.reflect == 'h':
                self.reflect = ' '
            else:
                self.reflect = 'h'
            self.images['defense'][int(self.frame)].clip_composite_draw(0, 0, 31, 21, 0, self.reflect, self.x, self.y, 70, 60)
            self.x_size = 70
            self.y_size = 60
        elif self.chance:
            self.images['chance'][int(self.frame)].clip_composite_draw(0, 0, 50, 50, 0, self.reflect, self.x, self.y,
                                                                        70, 60)
            self.x_size = 70
            self.y_size = 60
        elif self.hp <= 0:
            self.images['dead'][int(self.frame)].clip_composite_draw(0, 0, 50, 50, 0, self.reflect, self.x, self.y,
                                                                       70, 60)
            self.x_size = 70
            self.y_size = 60

        else:
            if math.cos(self.dir) < 0:
                self.reflect = 'h'
            else:
                self.reflect = ' '
            self.images['walk'][int(self.frame)].clip_composite_draw(0, 0, 32, 37, 0, self.reflect, self.x, self.y,
                                       70, 70)
            self.x_size = 70
            self.y_size = 70
        self.font.draw(self.x - 20, self.y - 50, 'HP %d' % self.hp, (255, 255, 255))

        draw_rectangle(*self.get_bb())
        pass
    def get_bb(self):
        return self.x - self.x_size//2, self.y - self.y_size//2, self.x + self.x_size//2, self.y + self.y_size//2

    def handle_collision(self, other, group, pos):
        if group =='bowser:ground':
            if pos == 'bottom':
                self.y -= self.pre_velocity * JUMP_SPEED_PPS * game_framework.frame_time
                self.y_velocity = 0
                self.pre_velocity = 0
        if self.hp > 0:
            if group == 'player:bowser' and not other.die:
                if pos == 'bottom':
                    if not self.defense:
                        if self.chance:
                            self.hp -= 5
                        else:
                            self.hp -= 2
                        if server.player.x <= self.x:
                            self.x += 15
                        else:
                            self.x -= 15
                    if random.randint(2, 10) % 2 == 1:
                        self.defense = True
                        self.hard = True


            if group == 'fire:bowser':
                game_world.remove_object(other)
                if not self.defense:
                    if self.chance:
                        self.hp -= 8
                    else:
                        self.hp -= 3
                    if server.player.x < self.x:
                        self.x += 15
                    else:
                        self.x -= 15

                if random.randint(1, 100) % 9 == 0:
                    self.defense = True
                    self.hard = True








