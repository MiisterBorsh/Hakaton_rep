import pygame
import random
from . import config, map, sprites, terrain

# Put in the x and y width and height (0 is not included) and this goes from left to right and then top to bottom (like reading a book)
def crop(surface, num_x, num_y):
    images = []
    for y in range(num_y):
        for x in range(num_x):
            images.append(surface.subsurface(x * config.TILE_WIDTH, y * config.TILE_WIDTH, config.TILE_WIDTH, config.TILE_WIDTH))
    return images

    #return [surface.subsurface(0, 0, config.TILE_WIDTH, config.TILE_WIDTH), surface.subsurface(config.TILE_WIDTH, 0, config.TILE_WIDTH, config.TILE_WIDTH), surface.subsurface(0, config.TILE_WIDTH, config.TILE_WIDTH, config.TILE_WIDTH), surface.subsurface(config.TILE_WIDTH, config.TILE_WIDTH, config.TILE_WIDTH, config.TILE_WIDTH)]

# Ground Tiles
path_center = pygame.transform.scale(pygame.image.load('src/Textures/path/path_center.png'), (config.TILE_WIDTH, config.TILE_WIDTH))
path_corner = pygame.transform.scale(pygame.image.load('src/Textures/path/path_corners.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH * 2))
path_corners = crop(path_corner, 2, 2)
path_one_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/path/path_one_sided.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH * 2))
path_one_sided = crop(path_one_sided_overall, 2, 2)
path_two_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/path/path_two_sided.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH))
path_two_sided = crop(path_two_sided_overall, 2, 1)
path_three_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/path/path_three_sided.png'), (config.TILE_WIDTH * 4, config.TILE_WIDTH * 4))
path_three_sided = crop(path_three_sided_overall, 4, 4)
path_four_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/path/path_four_sided.png'), (config.TILE_WIDTH * 4, config.TILE_WIDTH * 4))
path_four_sided = crop(path_four_sided_overall, 4, 4)

water_center = pygame.transform.scale(pygame.image.load('src/Textures/water/water_center.png'), (config.TILE_WIDTH, config.TILE_WIDTH))
water_corner = pygame.transform.scale(pygame.image.load('src/Textures/water/water_corners.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH * 2))
water_corner_solid = pygame.transform.scale(pygame.image.load('src/Textures/water/water_corners_solid.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH * 2))
water_corners = crop(water_corner, 2, 2)
water_corners_solid = crop(water_corner_solid, 2, 2)
water_one_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/water/water_one_sided.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH * 2))
water_one_sided = crop(water_one_sided_overall, 2, 2)
water_two_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/water/water_two_sided.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH))
water_two_sided = crop(water_two_sided_overall, 2, 1)
water_three_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/water/water_three_sided.png'), (config.TILE_WIDTH * 4, config.TILE_WIDTH * 4))
water_three_sided = crop(water_three_sided_overall, 4, 4)
water_four_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/water/water_four_sided.png'), (config.TILE_WIDTH * 4, config.TILE_WIDTH * 4))
water_four_sided = crop(water_four_sided_overall, 4, 4)

farmland_center = pygame.transform.scale(pygame.image.load('src/Textures/farmland/farmland_center.png'), (config.TILE_WIDTH, config.TILE_WIDTH))
farmland_corner = pygame.transform.scale(pygame.image.load('src/Textures/farmland/farmland_corners.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH * 2))
farmland_corner_solid = pygame.transform.scale(pygame.image.load('src/Textures/farmland/farmland_corners_solid.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH * 2))
farmland_corners = crop(farmland_corner, 2, 2)
farmland_corners_solid = crop(farmland_corner_solid, 2, 2)
farmland_one_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/farmland/farmland_one_sided.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH * 2))
farmland_one_sided = crop(farmland_one_sided_overall, 2, 2)
farmland_two_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/farmland/farmland_two_sided.png'), (config.TILE_WIDTH * 2, config.TILE_WIDTH))
farmland_two_sided = crop(farmland_two_sided_overall, 2, 1)
farmland_three_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/farmland/farmland_three_sided_2.png'), (config.TILE_WIDTH * 4, config.TILE_WIDTH * 4))
farmland_three_sided = crop(farmland_three_sided_overall, 4, 4)
farmland_four_sided_overall = pygame.transform.scale(pygame.image.load('src/Textures/farmland/farmland_four_sided.png'), (config.TILE_WIDTH * 4, config.TILE_WIDTH * 4))
farmland_four_sided = crop(farmland_four_sided_overall, 4, 4)


path_images = [path_center, path_corners, path_corners, path_one_sided, path_two_sided, path_three_sided, path_four_sided]
water_images = [water_center, water_corners, water_corners_solid, water_one_sided, water_two_sided, water_three_sided, water_four_sided]
farmland_images = [farmland_center, farmland_corners, farmland_corners_solid, farmland_one_sided, farmland_two_sided, farmland_three_sided, farmland_four_sided]

stone_light = pygame.transform.scale(pygame.image.load('src/Textures/stone.png'), (config.TILE_WIDTH, config.TILE_WIDTH))

dark = pygame.transform.scale(pygame.image.load('src/Textures/blocks/stone/dark.png'), (config.TILE_WIDTH, config.TILE_WIDTH))

# Blocks
stone_dark_front = {"name": 'dark_stone', "material": 'stone', "type": 'block', "image": pygame.transform.scale(pygame.image.load('src/Textures/blocks/stone/stone_dark_front.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}
stone_dark_side = {"name": 'dark_stone', "material": 'stone', "type": 'block', "image": pygame.transform.scale(pygame.image.load('src/Textures/blocks/stone/stone_dark_side.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}
stone_dark_images = [stone_dark_front, stone_dark_side]
crafting_bench = {"name": 'crafting_bench', "material": 'wood', "type": 'block', "image": pygame.transform.scale(pygame.image.load('src/Textures/crafting_bench.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}
hedge_front = {"name": 'hedge', "material": 'unbreakable', "type": 'block', "image": pygame.transform.scale(pygame.image.load('src/Textures/blocks/hedge/hedge_front2.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}
hedge_side = {"name": 'hedge', "material": 'unbreakable', "type": 'block', "image": pygame.transform.scale(pygame.image.load('src/Textures/blocks/hedge/hedge_side.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}
hedge_images = [hedge_front, hedge_side]

# Doors
hedge_door = {"name": 'hedge_door', "material": 'unbreakable', "type": 'door', "image": pygame.transform.scale(pygame.image.load('src/Textures/blocks/hedge/hedge_door_front.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}
stairs_up = {"name": 'down_stair', "material": 'stone', "type": 'door', "image": pygame.transform.scale(pygame.image.load('src/Textures/stairs/stairs_up.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}
stairs_down = {"name": 'down_stair', "material": 'stone', "type": 'door', "image": pygame.transform.scale(pygame.image.load('src/Textures/stairs/stairs_down.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}
stairs_left = {"name": 'down_stair', "material": 'stone', "type": 'door', "image": pygame.transform.scale(pygame.image.load('src/Textures/stairs/stairs_left.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}
stairs_right = {"name": 'down_stair', "material": 'stone', "type": 'door', "image": pygame.transform.scale(pygame.image.load('src/Textures/stairs/stairs_right.png'), (config.TILE_WIDTH, config.TILE_WIDTH))}

stairs_images = [stairs_up, stairs_down, stairs_left, stairs_right]

# Maps
overworld_layers = [map.overworld, map.overworld_layer_1]


# Handles all the collisions with tiles that need it by making hitboxes -- maybe too many arguments here
class Tile_Collisions(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image, surface, x_offset, y_offset, name):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = pygame.Rect(self.x * config.TILE_WIDTH, self.y * config.TILE_WIDTH, self.width, self.height)

        self.name = 'tile'

        if name == 'water':
            self.hitbox = pygame.Rect(self.x * config.TILE_WIDTH, self.y * config.TILE_WIDTH, self.width, self.height)
        if name == 'crafting bench':
            self.hitbox = pygame.Rect(self.x * config.TILE_WIDTH, self.y * config.TILE_WIDTH, self.width, self.height)
        if name == 'hedge':
            self.hitbox = pygame.Rect(self.x * config.TILE_WIDTH, self.y * config.TILE_WIDTH, self.width, self.height)
        if name == 'stairs':
            self.hitbox = pygame.Rect(self.x * config.TILE_WIDTH, self.y * config.TILE_WIDTH - (config.TILE_WIDTH / 4), self.width, self.height)

    def update(self, x_offset, y_offset):
        self.hitbox.topleft = self.x, self.y

tile_collisions_group = pygame.sprite.Group()

# def update_groups(area, x_offset, y_offset):
#     for sprite in sprites.obstacle_sprites:
#         if sprite.name != 'player':
#             if sprite.rect.x < x_offset:
#                 sprite.kill()

#             if sprite.name == 'tree':
#                 if area[1][sprite.y + 1][sprite.x] != 't':
#                     sprite.kill()


#     for sprite in sprites.visible_sprites:
#         if sprite.name != 'player':
#             if sprite.rect.x < x_offset:
#                 sprite.kill()

#             if sprite.name == 'tree':
#                 if area[1][sprite.y + 1][sprite.x] != 't':
#                     sprite.kill()
                

# Creates objects like trees by scanning through the overworld map -- arguments could be improved and also change the map so that it could be a variable

def check_surroundings(area, x, y, id):
    try:
        if area[y][x - 1] == id or area[y][x + 1] == id or area[y - 1][x] == id or area[y + 1][x] == id or area [y - 1][x - 1] == id or area[y - 1][x + 1] == id or area[y + 1][x - 1] == id or area[y + 1][x + 1] == id:
            return True
        else:
            return False
    except:
        pass
    else:
       return False

def create_objects_random(area, type, number):
    if type == 'tree':
        for i in range(number):
            x_loc = random.randint(0, len(area[1][0]) - 2)
            y_loc = random.randint(0, len(area[1]) - 2)
            if area[0][y_loc + 1][x_loc] == '0' and area[1][y_loc + 1][x_loc] == ' ':
                tree_object = sprites.Tree(x_loc, y_loc, config.TILE_WIDTH, config.TILE_WIDTH * 2)
                sprites.obstacle_sprites.add(tree_object)
                sprites.visible_sprites.add(tree_object)
                area[1][y_loc + 1][x_loc] = 't'

def BlockID(id):
    if id == 'H':
        return hedge_door
    if id == 'c':
        return crafting_bench
    if id == 'h':
        return hedge_images[0]
    if id == 's':
        return stairs_up
    if id == '#':
        return stone_dark_images[0]
    
    return hedge_images[0]
    

# This gets the tile id and returns the tile image which is drawn in main.py
def TileID(id, x, y, area, surface, x_offset, y_offset):
    if id == '0': return grass
    if id == '1': return create_path(id, x, y, area, path_images)
    if id == 'w': 
        water_collisions = Tile_Collisions(x, y, config.TILE_WIDTH, config.TILE_WIDTH, create_path(id, x, y, area, water_images), surface, x_offset, y_offset, 'water')
        sprites.obstacle_sprites.add(water_collisions)
        return create_path(id, x, y, area, water_images)
    if id == 'f':
        return create_path(id, x, y, area, farmland_images)
    
    if id == 'c':
        crafting_bench_collisions = Tile_Collisions(x, y, config.TILE_WIDTH, config.TILE_WIDTH, crafting_bench.get("image"), surface, x_offset, y_offset, 'crafting bench')
        sprites.obstacle_sprites.add(crafting_bench_collisions)
        sprites.visible_sprites.add(crafting_bench_collisions)
        return crafting_bench.get("image")
    if id == 'h':
        hedge_collisions = Tile_Collisions(x, y, config.TILE_WIDTH, config.TILE_WIDTH, create_blocks(id, x, y, area, hedge_images), surface, x_offset, y_offset, 'hedge')
        sprites.obstacle_sprites.add(hedge_collisions)
        sprites.visible_sprites.add(hedge_collisions)
        return create_blocks(id, x, y, area, hedge_images)
    
    if id == 't':
        tree_object = sprites.Tree(x, y - 1, config.TILE_WIDTH, config.TILE_WIDTH * 2)
        sprites.obstacle_sprites.add(tree_object)
        sprites.visible_sprites.add(tree_object)

    if id == 'H':
        hedge_collisions = Tile_Collisions(x, y, config.TILE_WIDTH, config.TILE_WIDTH, hedge_door.get("image"), surface, x_offset, y_offset, 'hedge')
        sprites.obstacle_sprites.add(hedge_collisions)
        sprites.visible_sprites.add(hedge_collisions)
        return hedge_door.get("image")
    
    if id == 's':
        stairs_collisions = Tile_Collisions(x, y, config.TILE_WIDTH, config.TILE_WIDTH, stairs_up.get("image"), surface, x_offset, y_offset, 'stairs')
        sprites.obstacle_sprites.add(stairs_collisions)
        sprites.visible_sprites.add(stairs_collisions)
        return stairs_up.get("image")
    
    if id == '+':
        return stone_light
    
    if id == '#':
        if check_surroundings(area, x, y, ' ') == True:
            stone_collisons = Tile_Collisions(x, y, config.TILE_WIDTH, config.TILE_WIDTH, create_blocks(id, x, y, area, stone_dark_images), surface, x_offset, y_offset, 'hedge')
            sprites.obstacle_sprites.add(stone_collisons)
            sprites.visible_sprites.add(stone_collisons)
            return create_blocks(id, x, y, area, stone_dark_images)
        else:
            dark_collisions = Tile_Collisions(x, y, config.TILE_WIDTH, config.TILE_WIDTH, dark, surface, x_offset, y_offset, 'hedge')
            sprites.obstacle_sprites.add(dark_collisions)
            sprites.visible_sprites.add(dark_collisions)
            return dark


def is_placeable(x, y, area):
    if area[0][y][x] == '0' or area[0][y][x] == '1' or area[0][y][x] == 'f':
        if area[1][y][x] == ' ':
            return True
    return False


def create_pond(area, num):
    for i in range(num):
        pond = terrain.create_terrain(8, 8, 30)

        x_loc = random.randint(0, len(area[0][0]) - 11)
        y_loc = random.randint(0, len(area[0]) - 11)

        for y in range(len(pond)):
            for x in range(len(pond[y])):
                #print(x, y)
                if pond[y][x] == '#' and area[1][y_loc][x_loc] != 'p':
                    #print(x, y)
                    area[0][y + y_loc][x + x_loc] = 'w'
                

def create_level(area):
    create_pond(area, 20)


def create_blocks(id, x, y, area, images):
    if y < len(area) - 1:
        if area[y + 1][x] == id:
            return images[1].get("image")
        else:
            return images[0].get("image")
    else:
        return images[0].get("image")
    # if y > 0:
    #     if area[y - 1][x] == id or area[y + 1][x] == id:
    #         return images[0].get("image")
    #     else:
    #         return images[1].get("image")
    # elif y < len(area):
    #     if area[y + 1][x] == id:
    #         return images[1].get("image")
    #     else:
    #         return images[0].get("image")

# This checks if there are any tiles next to it so that it can change the texture of the tile for design purposed
def create_path(id, x, y, area, images):
    path_matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    corners = [
        [0, 0],
        [0, 0]
    ]

    if area[y][x - 1] == id:
        path_matrix[1][0] = 1
    if area[y][x + 1] == id:
        path_matrix[1][2] = 1
    if area[y - 1][x] == id:
        path_matrix[0][1] = 1
    if area[y + 1][x] == id:
        path_matrix[2][1] = 1

    if area[y - 1][x - 1] == id:
        corners[0][0] = 1
    if area[y - 1][x + 1] == id:
        corners[0][1] = 1
    if area[y + 1][x - 1] == id:
        corners[1][0] = 1
    if area[y + 1][x + 1] == id:
        corners[1][1] = 1

    if path_matrix == [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]:
        return images[3][2]
    
    if path_matrix == [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]:
        return images[3][3]
    
    if path_matrix == [
        [0, 0, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]:
        return images[3][0]
    
    if path_matrix == [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]:
        return images[3][1]

    if path_matrix == [
        [0, 0, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]:
        if corners[1][0] == 1:
            return images[2][1]
        else:
            return images[1][1]
    
    if path_matrix == [
        [0, 0, 0],
        [0, 1, 1],
        [0, 1, 0]
    ]:
        if corners[1][1] == 1:
            return images[2][0]
        else:
            return images[1][0]
    
    if path_matrix == [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]:
        if corners[0][0] == 1:
            return images[2][3]
        else:
            return images[1][3]
    
    if path_matrix == [
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]:
        if corners[0][1] == 1:
            return images[2][2]
        else:
            return images[1][2]
    
    if path_matrix == [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]:
        return images[4][1]
    
    if path_matrix == [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]:
        return images[4][0]
    
    if path_matrix == [
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 0]
    ]:
        if corners[0][1] == 0 and corners[1][1] == 0:
            return images[5][2]
        elif corners[0][1] == 0:
            return images[5][0]
        elif corners[1][1] == 0:
            return images[5][1]
        else:
            return images[5][3]
    
    if path_matrix == [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]:
        if corners[0][0] == 0 and corners[0][1] == 0:
            return images[5][10]
        elif corners[0][0] == 0:
            return images[5][8]
        elif corners[0][1] == 0:
            return images[5][9]
        else:
            return images[5][11]
    
    if path_matrix == [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]:
        if corners[0][0] == 0 and corners[1][0] == 0:
            return images[5][6]
        elif corners[0][0] == 0:
            return images[5][4]
        elif corners[1][0] == 0:
            return images[5][5]
        else:
            return images[5][7]
    
    if path_matrix == [
        [0, 0, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]:
        if corners[1][0] == 0 and corners[1][1] == 0:
            return images[5][14]
        elif corners[1][0] == 0:
            return images[5][12]
        elif corners[1][1] == 0:
            return images[5][13]
        else:
            return images[5][15]
    
    if path_matrix == [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]:
        if corners[0][0] == 1 and corners[0][1] == 1 and corners[1][0] == 1 and corners[1][1] == 1:
            return images[6][10]
        elif corners[0][0] == 0 and corners[0][1] == 0 and corners[1][0] == 0 and corners[1][1] == 0:
            return images[6][11]
        elif corners[0][0] == 0 and corners[1][1] == 0 and corners[1][0] == 1 and corners[0][1] == 1:
            return images[6][8]
        elif corners[0][1] == 0 and corners[1][0] == 0 and corners[0][0] == 1 and corners[1][1] == 1:
            return images[6][9]
        elif corners[0][0] == 0 and corners[1][0] == 0 and corners[0][1] == 1 and corners[1][1] == 1:
            return images[6][12]
        elif corners[0][0] == 0 and corners[0][1] == 0 and corners[1][0] == 1 and corners[1][1] == 1:
            return images[6][13]
        elif corners[0][1] == 0 and corners[1][1] == 0 and corners[1][0] == 1 and corners[0][0] == 1:
            return images[6][15]
        elif corners[1][0] == 0 and corners[1][1] == 0 and corners[0][0] == 1 and corners[0][1] == 1:
            return images[6][14]
        
        elif corners[0][1] == 0 and corners[1][0] == 0 and corners[1][1] == 0:
            return images[6][4]
        elif corners[0][0] == 0 and corners[1][0] == 0 and corners[1][1] == 0:
            return images[6][5]
        elif corners[0][0] == 0 and corners[0][1] == 0 and corners[1][1] == 0:
            return images[6][6]
        elif corners[0][0] == 0 and corners[0][1] == 0 and corners[1][0] == 0:
            return images[6][7]
        elif corners[0][0] == 0:
            return images[6][0]
        elif corners[0][1] == 0:
            return images[6][1]
        elif corners[1][0] == 0:
            return images[6][2]
        elif corners[1][1] == 0:
            return images[6][3]

    return images[0]




grass = pygame.transform.scale(pygame.image.load('src/Textures/grass.png'), (config.TILE_WIDTH, config.TILE_WIDTH))