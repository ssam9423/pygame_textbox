# Pygame Textbox Class
## Description
This is a class to create textboxes in Pygame.

## Initializing a Textbox - Parameters and Variables
To initialize a Textbox, the following are required:
| Parameter | Type                            | Description                               |
|-----------|---------------------------------|-------------------------------------------|
|`screen`   | `pygame.surface.Surface`        | surface on which the Textbox is displayed |

The other parameters are optional:
| Parameter      | Type      | Description                                                                                                                       |
|----------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
|`name`          | `string`  | text desplayed in the Textbox when empty and not clicked on                                                                       |
|`x_pos`         | `int`     | x-position of the Textbox                                                                                                         |
|`y_pos`         | `int`     | y-position of the Textbox                                                                                                         |
|`cursor_width`  | `int`     | width of the cursor when typing in the Textbox                                                                                    |
|`b_radius`      | `int`     | radius of Button corners - for rounded corners                                                                                    |
|`bg_color`      | `tuple`   | background color of the Textbox                                                                                                   |
|`t_color`       | `tuple`   | text color of the Textbox                                                                                                         |
|`empty_t_color` | `tuple`   | text color of the Textbox when empty and not clicked on                                                                           |
|`font_name`     | `string`  | name of font for Textbox text                                                                                                     |
|`font_size`     | `int`     | size of font for Textbox text                                                                                                     |
|`width`         | `int`     | width of Textbox                                                                                                                  |
|`height`        | `int`     | height of Textbox                                                                                                                 |
|`spacing_factor`| `int`     | factor determining the spacing size between the text on the Textbox and the Textbox (based on `height`)                           |
|`static_size`   | `Boolean` | determines if the size of the button adjusts with a change in screen size                                                         |
|`value`         | `string`  | the initial value in the Textbox                                                                                                  |
|`on`            | `Boolean` | determines if the Textbox allows user to input text (at initialization, determines if user can input text when the program starts |

## Functions
The Textbox class has multiple functions:
| Function Name               | Parameter Type                  | Description                                                           |
|-----------------------------|---------------------------------|-----------------------------------------------------------------------|
|`show(event.pos)`            | `tuple`                         |draws Textbox and appropriate text depending on if the Textbox is `on`.|
|`clear()`                    |                                 | this function clears the `value` of the Textbox.                      |
|`tb_click(mouse_pos)`        | `tuple`                         | this function determines whether a Textbox should be `on` based on where the user clicks (inside or outside the Textbox). |
|`get_value()`                |                                 | this function returns the `value` of the Textbox
|`update_screen(screen)`      | `pygame.surface.Surface`        | this funtion updates screen on which the Textbox is displayed on. If `static_size` is `False`, the Textbox's `width` and `height` are updated as well. |
|`auto_font_size()`           |                                 | this function updates the font size so that the text on the Textbox fits within the Textbox according to the Textbox's `spacing`|
|`update_spacing(new_spacing)`| `int`                           | this function takes in an integer as the new `spacing_factor` and updates the `spacing`|
|`get_size_offset()`          |                                 | this function returns a pair of integers representing the offset from the Textbox's center |
|`get_size()`                 |                                 | this function returns a pair of integers representing the `width` and `height` of the Textbox |
|`get_font_size()`            |                                 | this function returns a pair or integers representing the width and height of the text on the Textbox |


## Example Code
```
import pygame
pygame.init()
# Initialize Screen & Allow for Resizing
screen = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
# Pygame now allows natively to enable key repeat:
pygame.key.set_repeat(200, 25)
# Inititalize Textboxes
test = Textbox(screen)
test2 = Textbox(screen, y_pos=100, value='test', on=False)

game_on = True
while game_on:
    screen.fill((232, 228, 218))
    events = pygame.event.get()
    # User Inputs - Necessary for multiple Textboxes or they share inputs
    if test.on:
        test.textinput.update(events)
    if test2.on:
        test2.textinput.update(events)

    for event in events:
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.VIDEORESIZE:
            # Updates Screen Size & Adjusts Textboxes to match
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            test.update_screen(screen)
            test.auto_font_size()
            test2.update_screen(screen)
            test2.auto_font_size()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # For clicking in and out of Textboxes
            test.tb_click(event.pos)
            test2.tb_click(event.pos)

    # Show Textboxes
    test.tb_show()
    test2.tb_show()
    # Update Screen
    pygame.display.update()
```

## Acknowledgements
The Textbox Class relies on [Pygame Text Input Module](https://github.com/Nearoo/pygame-text-input) by [Nearoo](https://github.com/Nearoo/).
