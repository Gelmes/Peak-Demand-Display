
class Battery:
    def __init__(self, screen, x=0, y=0, width=100,height=500):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self. hegith = height
        self.image = self.screen.load_image('bat.png')
        self.image = self.screen.scale(self.image, width, height)
        self.soc  = 15.0
        self.top_margin = 38.0 #used to limit image from green going too high
        self.bottom_margin = 10
        self.green = (0,250,0)

    def set_soc(self, soc):
        self.soc = soc

    def draw(self):
        #y = self.y+self.top_margin+((self.image.get_height()-self.top_margin+3)*(1 - self.soc / 100.0))
        #h = (self.image.get_height()*(self.soc / 100.0))-self.top_margin
        height = self.image.get_height() - self.top_margin - self.bottom_margin
        soc = (1 - self.soc/100.0)
        y = self.y+self.top_margin + (height * soc)
        h = self.image.get_height() - self.top_margin - self.bottom_margin - height * soc      
        rect = [self.x+5, y,self.image.get_width()-10, h]
        self.screen.draw_rectangle(self.green, rect)
        self.screen.draw_image(self.image, (self.x, self.y))
        

    
        
