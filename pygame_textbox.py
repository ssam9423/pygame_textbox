# Textbox Module for Pygame 
import pygame
import pygame_textinput as pyti

# Defaults
stop_type = pyti.TextInputManager(validator=lambda input: False)

class Textbox:
    def __init__(self, screen, name='Textbox', x_pos=0, y_pos=0,
                 cursor_width=4, b_radius=2, 
                 bg_color=(196, 183, 164), t_color=(40, 54, 24),
                 empty_t_color=(232, 228, 218),
                 font_name='yugothicuisemibold', font_size=40,
                 width=600, height=55, spacing_factor=10,
                 static_size=False, value='', on=True):
        self.name = name
        self.screen = screen
        self.b_radius = b_radius
        self.bg_color = bg_color
        self.t_color = t_color
        self.empty_t_color = empty_t_color

        self.font_name = font_name
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.width = width
        self.height = height
        self.w_factor = self.screen.get_size()[0] / self.width
        self.h_factor= self.screen.get_size()[1] / self.height
        self.spacing_factor = spacing_factor
        self.spacing = self.height / self.spacing_factor

        self.font_x_pos = self.x_pos + self.spacing
        self.font_y_pos = self.y_pos + self.spacing

        self.textinput = pyti.TextInputVisualizer()
        self.textinput.cursor_width = cursor_width
        self.tb_manager = pyti.TextInputManager(validator=lambda input: 
                                   (self.font.render(input, 1, self.t_color).get_size()[0] +
                                    self.textinput.cursor_width < (self.width - 2*self.spacing)))
        self.textinput.manager = self.tb_manager

        self.textinput.font_color = t_color
        self.textinput.font_object = self.font
        self.font_height = self.textinput.font_object.get_height()

        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.static_size = static_size
        self.value = value
        self.on = on
    
    def tb_box_draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.rect, border_radius=self.b_radius)

    def tb_text_blit(self):
        if self.on:
            self.screen.blit(self.textinput.surface, 
                             (self.font_x_pos, self.font_y_pos))
        else:
            if self.value == '' and self.textinput.value == '':
                self.screen.blit(self.font.render(self.name, 1, self.empty_t_color), 
                                 (self.font_x_pos, self.font_y_pos))
            else:
                self.screen.blit(self.font.render(self.value, 1, self.t_color), 
                                 (self.font_x_pos, self.font_y_pos))
                
    def show(self):
        self.tb_box_draw()
        self.tb_text_blit()
            
    def clear(self):
        self.textinput.value = ''
        self.value = ''

    def update_value(self):
        if self.textinput.value != '':
            self.value = self.textinput.value

    def tb_click(self, mouse_pos):
        # Click Inside Textbox
        if self.rect.collidepoint(mouse_pos):
            if not self.on:
                self.textinput.value = self.value
                self.textinput.manager = self.tb_manager
                # tb_manager holds prior textinput.value
                self.textinput.manager.left = self.value
                self.on = True
        # Click Outside Textbox
        else:
            if self.on:
                self.update_value()
                self.textinput.manager = stop_type
                # stop_type holds prior textinput.value
                self.textinput.value = self.value
                self.on = False
        
    def get_value(self):
        self.update_value()
        return self.value
    
    def update_screen(self, new_screen):
        self.screen = new_screen
        if not self.static_size:
            self.width = new_screen.get_size()[0] / self.w_factor
            self.height = new_screen.get_size()[1] / self.h_factor
            self.spacing = self.height / self.spacing_factor
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        
    def auto_font_size(self):
        curr_size = int(self.height)
        while curr_size > 1:
            f_w, f_h = pygame.font.SysFont(self.font_name, curr_size).size(self.name)
            if ((f_w < (self.width - (2 * self.spacing))) and
                (f_h < (self.height - (2 * self.spacing)))):
                break
            else:
                curr_size -= 1
        self.font_size = curr_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.textinput.font_object = self.font
        self.tb_manager = pyti.TextInputManager(validator=lambda input: 
                                   (self.font.render(input, 1, self.t_color).get_size()[0] +
                                    self.textinput.cursor_width < (self.width - 2*self.spacing)))

    def update_spacing(self, new_spacing):
        self.spacing_factor = new_spacing
        self.spacing = self.height / new_spacing

    def get_size_offset(self):
        return (int(self.width/2), int(self.height/2))
    
    def get_size(self):
        return (self.width, self.height)
    
    def get_font_size(self):
        return self.font.size(self.name)
