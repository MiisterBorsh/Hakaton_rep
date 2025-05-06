import pygame
import sys
from src import tiles, config, player, map, inventory, sprites, items, animations

pygame.init()
clock = pygame.time.Clock()

x_tiles = int(config.SCREEN_WIDTH / config.TILE_WIDTH)
y_tiles = int(config.SCREEN_HEIGHT / config.TILE_WIDTH)

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Sandbox Game")
inventory_opened = False

player_object = player.Player(64, 64, screen)
player_group = pygame.sprite.GroupSingle()
player_group.add(player_object)
transition = animations.Darkness()

sprites.visible_sprites.add(player_object)

paused = False

def initalize_level(area):
    for sprite in sprites.obstacle_sprites:
        if sprite.name != 'player':
            sprite.kill()
    for sprite in sprites.visible_sprites:
        if sprite.name != 'player':
            sprite.kill()

    if area[2] == False:
        tiles.create_level(area)
        tiles.create_objects_random(area, 'tree', 300)
    for y in range(len(area[1])):
        for x in range(len(area[1][y])):
            if area[1][y][x] == 'p':
                player_object.set_location(x * config.TILE_WIDTH, y * config.TILE_WIDTH)

    if player_object.current_area != map.underground_layers:
        if player_object.facing_direction[1] == -1:
            player_object.hitbox.bottom = (config.MAP_HEIGHT * config.TILE_WIDTH) - (config.TILE_WIDTH * 2)
        if player_object.facing_direction[1] == 1:
            player_object.hitbox.top = config.TILE_WIDTH * 2
    area[2] = True

initalize_level(map.current_area)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if inventory_opened == True:
                    inventory_opened = False
                    paused = False
                else: 
                    inventory_opened = True
                    paused = True

            if event.key == pygame.K_1:
                inventory.key_input(1)
            if event.key == pygame.K_2:
                inventory.key_input(2)
            if event.key == pygame.K_3:
                inventory.key_input(3)

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] and inventory_opened:
            inventory.mouse_x, inventory.mouse_y = pygame.mouse.get_pos()
            inventory.mouse_update('pressed')

        if event.type == pygame.MOUSEMOTION:
            inventory.mouse_x, inventory.mouse_y = pygame.mouse.get_pos()
            inventory.mouse_update('movement')

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                inventory.mouse_x, inventory.mouse_y = pygame.mouse.get_pos()
                inventory.mouse_update('released')

    x_offset = player_object.get_offset_x()
    y_offset = player_object.get_offset_y()

    screen.fill((0, 0, 0))

    for m in range(len(map.current_area) - 1):

        for y in range(int(((config.SCREEN_HEIGHT + y_offset) / config.TILE_WIDTH)) + 2):
            for x in range(int(((config.SCREEN_WIDTH + x_offset) / config.TILE_WIDTH)) + 2):
                try:

                    if (x + 2) * config.TILE_WIDTH > x_offset and (x - 2) * config.TILE_WIDTH < x_offset + config.SCREEN_WIDTH - config.TILE_WIDTH:
                        if (y + 2) * config.TILE_WIDTH > y_offset and (y - 2) * config.TILE_WIDTH < y_offset + config.SCREEN_HEIGHT - config.TILE_WIDTH:
                            if m == 0:
                                screen.blit(tiles.TileID(map.current_area[m][y][x], x, y, map.current_area[m], screen, x_offset, y_offset), ((x * config.TILE_WIDTH) - x_offset, (y * config.TILE_WIDTH) - y_offset))
                            if m > 0:
                                tiles.TileID(map.current_area[m][y][x], x, y, map.current_area[m], screen, x_offset, y_offset)
                except:
                    pass

    if paused == True:
         inventory.update(player_object.rect.x, player_object.rect.y, screen)
    else:
        player_group.update(inventory.slots[3][items.toolbar_selected_slot])

    sprites.visible_sprites.draw(screen, player_object)

    if inventory_opened == False: 
        inventory.toolbar(screen)
    else:
        inventory.update(player_object.rect.x, player_object.rect.y, screen)

    for sprite in sprites.obstacle_sprites:

        if sprite.name != 'player' and sprite.name != 'dropped_item':
            sprite.kill()
    for sprite in sprites.visible_sprites:
        if sprite.name != 'player' and sprite.name != 'dropped_item':
            sprite.kill()

    if map.current_area != player_object.current_area:
        transition.fade()
        if transition.alpha_index < 0:
            map.current_area = player_object.current_area
            initalize_level(map.current_area)

    transition.display()

    pygame.display.update()

    clock.tick(60)