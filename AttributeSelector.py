import pygame
import pygame_gui
import GenericConstants


class AttributeSelector:
    def __init__(self, name, init_value, manager, const_list):
        self.name = name
        self.init_value = init_value
        self.manager = manager
        self.label = self.create_label()
        self.up_button = self.create_up_button()
        self.down_button = self.create_down_button()
        self.field = self.create_field()

    def create_label():
        return pygame_gui.elements.UILabel(relative_rect = pygame.Rect((const_list[GenericConstants.LABEL_X],
                                                                        const_list[GenericConstants.LABEL_Y]),
                                                                       (GenericConstants.LABEL_WIDTH,
                                                                        GenericConstants.LABEL_HEIGHT)),
                                           text=self.name,
                                           manager=self.manager,
                                           container=None,
                                           parent_element=None,
                                           object_id=None,
                                           anchors=None,
                                           visible=1)

    def create_up_button():
        return pygame_gui.elements.UIButton(relative_rect = pygame.Rect((const_list[GenericConstants.UP_X],
                                                                         const_list[GenericConstants.UP_Y]),
                                                                        (GenericConstants.UP_BUTTON_WIDTH,
                                                                         GenericConstants.UP_BUTTON_HEIGHT)),
                                            text='>',
                                            manager=self.manager,
                                            container=None)
    def create_down_button():
        return pygame_gui.elements.UIButton(relative_rect = pygame.Rect((const_list[GenericConstants.DOWN_X],
                                                                         const_list[GenericConstants.DOWN_Y]),
                                                                        (GenericConstants.DOWN_BUTTON_WIDTH,
                                                                         GenericConstants.DOWN_BUTTON_HEIGHT)),
                                            text='<',
                                            manager=self.manager,
                                            container=None)
    def create_field():
        return_field = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((const_list[GenericConstants.FIELD_X],
                                                                                        const_list[GenericConstants.FIELD_Y]),
                                                                                       (GenericConstants.FIELD_WIDTH,
                                                                                        GenericConstants.FIELD_HEIGHT)),
                                                           manager=self.manager,
                                                           container=None)
        return_field.set_allowed_characters('numbers')
        return_field.set_text('0')
        return return_field
                            
    
