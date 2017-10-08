
class Value:
    """
    Creates a text value meant to be output to screen
    """
    def __init__(self, screen, x=0, y=0, label="Label: ", value=100):
        self.screen = screen
        self.x = x
        self.y = y
        self.value  = value
        self.label = label
        self.font_color = (200,200,200)
        self.font = self.screen.get_font(30, 'Arial')

    def set_color(self, color):
        self.font_color = color

    def set_value(self, value):
        self.value = value

    def set_label(self, label):
        self.label = label

    def draw(self):
        self.screen.draw_text(self.label + str(self.value), [self.x, self.y], self.font_color, font=self.font)
            
        

    
        
