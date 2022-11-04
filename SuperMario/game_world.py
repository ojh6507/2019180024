# game world

world = [[],[],[],[]]

def add_object(o, depth):
    world[depth].append(o)

def add_objects(ol, depth): # 많은 객체들 더하기 ol type: list
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Triying destory non exiting object')

def all_objects(): # generator 발전기라는 오브젝트로 취급
    for layer in world:
        for o in layer:
            yield o #yield가 있는 순간 함수로 취급X
def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()
