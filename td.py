import sys
import pygame
from settings import Settings
from button import Button
from tower import Tower
from tower_hovers import Tower_Hovers
from enemy import Enemy

class TowerDefense:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        
        # Go get the settings
        self.settings = Settings()
        

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tower Defense")

        # Set up the map
        self.map_image = pygame.image.load('images/map.bmp')
        self.map_rect = self.map_image.get_rect()

        # Create the first build tower button
        self.build_tower_button = Button(self)
        self.button_clicked = False # Was a button just clicked?

        # Initialize various game modes
        self.build_tower_mode = False
        self.pre_round_mode = True

        # Create the various sprite groups of the game
        self.towers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Go get the tower hover images
        self.tower_hovers = Tower_Hovers()




    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self._update_screen()
            

    def _check_events(self):
        """Respond to keyboard and mouse presses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
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


    def _build_tower(self, mouse_pos):
        """Build a tower where the user clicked."""
        tower = Tower(self, mouse_pos)

        # Check to make sure tower can only be built on grass.
         
        if mouse_pos[0] < 1175 and mouse_pos[1] < 775:
            grass = self._check_pixel_color(mouse_pos)
        else:
            grass = False

        if grass:
            # Add a check for rect collisions between tower and existing towers.
            tower_collision = self._check_tower_collisions(tower)
            if tower_collision == False:
                self.towers.add(tower)
                # Spawn an enemy for testing purposes.
                self._spawn_enemy()


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
            # Can build here
            # Change the color of the displayed tower to green. 
            self._make_green(self.tower_hovers.basic_tower_image)
            if self._check_tower_collisions(tower) == True:
                self._make_red(self.tower_hovers.basic_tower_image)            
        else:
            # Not Grass
            # Change the color back to normal or to red!
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
        
        # Carry out the button functions depending on which button was clicked.
        if new_tower_clicked:
            self.build_tower_button.toggle_button()
            self._toggle_mode()
            self.button_clicked = True


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

    
    def _update_screen(self):
        """Update images on screen, flip to new screen."""

        self.screen.fill(self.settings.bg_color) # can remove once the map is done
        # Draw the map
        self.screen.blit(self.map_image, self.map_rect)
        self.build_tower_button.draw_button() # eventually probably have a function that draws all buttons.

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
