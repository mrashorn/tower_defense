import sys
import pygame
from settings import Settings
from button import Button
from tower import Tower
from tower_hovers import Tower_Hovers
from enemy import Enemy
import math

class TowerDefense:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        
        # Go get the settings
        self.settings = Settings()

        # Get the enemy walking path
        pathFile = open('path.txt')
        self.enemy_path = pathFile.readlines()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tower Defense")

        # Set up the map
        self.map_image = pygame.image.load('images/map.bmp')
        self.map_rect = self.map_image.get_rect()

        # Create the first build tower button
        self.build_tower_button = Button(self, 'images/build_tower.bmp', 650, 850)
        self.start_round_button = Button(self, 'images/start_round.bmp', 850, 850)

        # Initialize various game modes
        self.build_tower_mode = False
        self.pre_round_mode = True
        self.live_round_mode = False

        # Create the various sprite groups of the game
        self.towers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Go get the tower hover images
        self.tower_hovers = Tower_Hovers()

        # Game Feature Statuses
        self.enemies_alive = False
        self.button_clicked = False # Was a button just clicked?



    def run_game(self):
        """Start the main game loop."""
        self.counter = 1
        while True:
            self._check_events()
            self._check_enemy_status()
            self._update_enemies()
            self._update_screen()
            if self.counter > 75:
                sys.exit()


    def _check_events(self):
        """Respond to keyboard and mouse presses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # check what mode we are in mode = check_mode(self)
                # if mode = build tower
                      # build tower functions (mouse pos)
                # if mode = live round mode
                    # clicking during live round (mouse pos)
                
                # If we just clicked a button, don't do anything except exit the mode
                self._check_button_clicked(mouse_pos)
                if self.button_clicked:
                    continue


                if self.build_tower_mode == True:
                    self._build_tower(mouse_pos)


    def _check_enemy_status(self):
        """Check if any enemies are left alive."""
        if self.enemies:
            self.enemies_alive = True
        else:
            self.enemies_alive = False


    def _update_enemies(self):
        """Check and update all enemy locations, move enemies along path."""
        for enemy in self.enemies:
            # Get the enemy location
            enemy_location = enemy.rect.center
            # Get the next location they are going to
            next_dest = self._get_next_dest(enemy)
            # calculate the direction to travel 
            travel_direction = self._get_travel_direction(enemy_location, next_dest)
            # travel
            # I think you only do one "unit" or frame of movement here. 
            enemy.rect.center = self._enemy_travel(enemy_location, travel_direction)
            self.counter += 1
            # check for if they made it
            # Mark that checkpoint True
            print("Here is this enemies checkpoint list!")
            print(enemy.checkpoints)


    def _get_next_dest(self, enemy):
        """Find which checkpoint is next to travel to for the enemy."""
        for checkpoint in enemy.checkpoints:
            if checkpoint == False:
                # Get the checkpoints index
                index = enemy.checkpoints.index(checkpoint)
                # Get the coordinate from the enemy_path, strip the ends
                coordinate = self.enemy_path[index].strip()[1:-2]
                # Get the specific X and Y values
                x_coord = int(coordinate[:coordinate.index(",")])
                y_coord = int(coordinate[coordinate.index(",") + 2:])
                return(x_coord, y_coord)


    def _get_travel_direction(self, enemy_location, next_dest):
        """Find the travel vector based on location and next destination."""
        # enemy current coordinates
        enemy_x_coord = enemy_location[0]
        enemy_y_coord = enemy_location[1]
        # coordinates of next point in the path
        next_x = next_dest[0]
        next_y = next_dest[1]
        # the difference between those two positions
        delta_x = next_x - enemy_x_coord
        delta_y = next_y - enemy_y_coord
        # Solve for theta
        theta = math.atan(delta_y/delta_x)
        return theta

    def _enemy_travel(self, enemy_location, theta):
        """Move the enemy in the travel direction."""
        enemy_x_coord = enemy_location[0]
        enemy_y_coord = enemy_location[1]
        enemy_new_x = enemy_x_coord + (self.settings.enemy_speed * math.cos(theta))
        enemy_new_y = enemy_y_coord + (self.settings.enemy_speed * math.sin(theta))
        print("Enemy new x position is " + str(enemy_new_x))
        print("Enemy new y position is " + str(enemy_new_y))
        return (enemy_new_x, enemy_new_y)





    def _build_tower(self, mouse_pos):
        """Build a tower where the user clicked."""
        tower = Tower(self, mouse_pos)

        # Only allow tower placement inside map area and on grass.
        if mouse_pos[0] < 1175 and mouse_pos[1] < 775:
            grass = self._check_pixel_color(mouse_pos)
        else:
            grass = False

        if grass:
            # Check for tower collisions.
            tower_collision = self._check_tower_collisions(tower)
            if tower_collision == False:
                self.towers.add(tower)


    def _check_pixel_color(self, mouse_pos):
        """Check the color of the pixel to see if a tower can be placed there."""
        pixel_color = self.map_image.get_at((mouse_pos[0], mouse_pos[1]))

        # Check for green color
        if pixel_color[0] < 110 and pixel_color [1] > 90:
            return True
        else:
            return False


    def _check_tower_collisions(self, tower):
        """Check if the newly placed tower will collide with an existing tower."""
        for placed_tower in self.towers:
            if pygame.sprite.collide_rect(tower, placed_tower):
                return True
        return False

    


    def _display_tower(self):
        """Display the selected tower as the mouse is moved around."""
        mouse_pos = pygame.mouse.get_pos()
        self.tower_hovers.basic_tower_rect.center = mouse_pos
        tower = Tower(self, mouse_pos)

        # if mouse outside map, grass = F
        # If mouse is outside bounds of map, check the screen. 
        if mouse_pos[0] > 1175 or mouse_pos[1] > 775:
            grass = False
        else:
            # If grass, change color of tower hover to green.
            grass = self._check_pixel_color(mouse_pos)

        if grass:
            # Change the color of the displayed tower to green. 
            self._make_green(self.tower_hovers.basic_tower_image)
            if self._check_tower_collisions(tower) == True:
                self._make_red(self.tower_hovers.basic_tower_image)            
        else:
            # Not Grass
            # Change the color back to red
            self._make_red(self.tower_hovers.basic_tower_image)            
            
        self.screen.blit(self.tower_hovers.basic_tower_image, self.tower_hovers.basic_tower_rect)
        self._display_tower_range(mouse_pos)

        
    def _display_tower_range(self, mouse_pos):
        """Display the range of the tower as you try to place it on map."""
        tower = Tower(self, mouse_pos)
        pygame.draw.circle(self.screen, (255, 255, 255), mouse_pos, tower.range, width=1)



    def _make_green(self, tower_image):
        """Add a green tint to the hovered tower image."""
        w, h = tower_image.get_size()
        for x in range(w):
            for y in range(h):
                pixel_color = tower_image.get_at((x,y))
                if  pixel_color != (255, 255, 255, 255): # anything but the background of the image
                    tower_image.set_at((x,y), pygame.Color(0, 250, 0))


    def _make_red(self, tower_image):
        """Add a red tint to the hovered tower image."""
        w, h = tower_image.get_size()
        for x in range(w):
            for y in range(h):
                pixel_color = tower_image.get_at((x,y))
                if pixel_color != (255, 255, 255, 255): # anything but the background of the image
                    tower_image.set_at((x,y), pygame.Color(250, 0, 0))


    def _spawn_enemy(self):
        """Spawn an enemy at the spawn location on the map."""
        enemy = Enemy(self)
        self.enemies.add(enemy)

                
    def _check_button_clicked(self, mouse_pos):
        """Check if the mouse clicked any of the game's buttons."""
        self.button_clicked = False # Reset the button check before we check for buttons

        # Check which button we clicked.
        new_tower_clicked = self.build_tower_button.rect.collidepoint(mouse_pos)
        start_round_clicked = self.start_round_button.rect.collidepoint(mouse_pos)
        
        # Carry out the button functions depending on which button was clicked.
        if new_tower_clicked:
            self.build_tower_button.toggle_button()
            self._toggle_mode()
            self.button_clicked = True

        if start_round_clicked:
            self.live_round_mode = True
            self._start_round(1)
            self.start_round_button.remove_button()


    def _start_round(self, current_level):
        """Start the round by spawning enemies based on the current game level."""
        for i in range(current_level):
            self._spawn_enemy()
            print(f"Starting level {i+1}!")



    def _toggle_mode(self):
        """toggle the new mode that we just entered."""
        if self.build_tower_button.toggle_status == True:
            self.build_tower_mode = True
            self.pre_round_mode = False
        else:
            self.build_tower_mode = False
            self.pre_round_mode = True


    def _check_hover(self):
        """Check to see if mouse is hovering a placed tower."""
        mouse_pos = pygame.mouse.get_pos()
        for tower in self.towers:
            if pygame.Rect.collidepoint(tower.rect, mouse_pos):
                # display the tower range.
                self._display_tower_range(tower.rect.center) # Send tower.rect.center instead of mouse pos


    def _draw_buttons(self):
        """Draw all the games buttons."""
        self.build_tower_button.draw_button()
        if self.live_round_mode == False:
            self.start_round_button.draw_button()

    
    def _update_screen(self):
        """Update images on screen, flip to new screen."""

        self.screen.fill(self.settings.bg_color) # can remove once the map is done
        # Draw the map
        self.screen.blit(self.map_image, self.map_rect)
        self._draw_buttons()

        self.towers.draw(self.screen)
        self.enemies.draw(self.screen)

        if self.build_tower_mode == True:
            self._display_tower()
        elif self.pre_round_mode == True: # only in pre-round mode, not when placing a tower.
            self._check_hover()

            


        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    td = TowerDefense()
    td.run_game()
