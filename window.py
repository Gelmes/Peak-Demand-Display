
class Window:
    def __init__(self, screen, x=0, y=0, width=800, height=480):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = [self.x, self.y, self.width, self.height]

        self.charts = [] #data charts
        self.scaled_chart_data = []

        self.y_shift = self.height/2 + self.y
        self.x_zoom = 1
 
        self.screen = screen
        self.border_color = (100,100,100)
        self.font_color = (100,100,100)
        self.border_width = 2

        #Axis Stuff
        self.last_label = "0"
        self.max_y = 0
        self.max_x = 0
        self.num_x_axis = 5 # always pick a prime to have the zero axis
        self.num_y_axis = 5
        self.axis_color = (255,255,255) #White
        self.axis_width = 2
        self.x_array = [] # A temporary axis array used for scrolling along
        self.x_index = 0  #used in the modulo calculation for a circular array
        self.x_prev_modulo = 0
        
        for val in range(self.num_y_axis):
            self.x_array.append([(-1 * self.width * self.x_zoom * self.x), "0"])

    def set_all_colors(self, color):
        self.axis_color = color
        self.font_color = color
        self.border_color = color

    def set_axis_color(self, color):
        self.axis_color = color

    def set_font_colot(self, color):
        self.font_color = color

    def set_border_color(self, color):
        self.border_color = color

    def set_border_width(self, width):
        self.border_width = width

    def set_axis_width(self, width):
        self.axis_width = width

    def draw_x_axis(self, axis_text=1):
        """
        Make this work
        name is backwards but this draws the vertical axis lines.
        """
        
        #counter = self.max_x
        #step = self.width/float(self.num_y_axis+1)
        modulo = self.max_x % (self.width / self.num_y_axis/ self.x_zoom)
        if (modulo < self.x_prev_modulo):
            self.x_index = (self.x_index + 1) % self.num_y_axis
            self.x_array[self.x_index] = [self.max_x, self.last_label]
        self.x_prev_modulo = modulo

        y1 = self.y
        y2 = self.y + self.height
        
        for val in self.x_array:
            x = self.width - ((self.max_x - val[0]) * self.x_zoom) + self.x
            self.screen.draw_line(self.axis_color, [x,y1], [x,y2], self.axis_width)
            if(axis_text):
                self.screen.draw_text(str(val[1]), [x, y2], self.font_color, vertical=1)
            

    def draw_y_axis(self, axis_text=1, snap=1):
        """
        draws the horizontal axis lines
        Snapping causes the axis to stick to specific rounded values factors of 2

        this kind of assumes that the Y shift is set to be in the middle
        """
        if(snap):
                step = self.find_scale(self.max_y, (self.num_y_axis-1)/2)
                counter = 0 
                while(counter < self.max_y):

                    try:
                        y_pos = ((-1 * (counter/float(self.max_y))) * (self.height/2) + self.y_shift)
                        y_neg = ((-1 * ((-1 * counter)/float(self.max_y))) * (self.height/2) + self.y_shift)
                    except ZeroDivisionError:
                        y_pos = ((-1 * (counter/1.0)) * (self.height/2) + self.y_shift)
                        y_neg = ((-1 * ((-1 * counter)/1.0)) * (self.height/2) + self.y_shift)                    
                    
                    start = [self.x, y_pos]
                    stop = [self.x + self.width + 10, y_pos]
                    self.screen.draw_line(self.axis_color, start, stop, self.axis_width)                    
                    start = [self.x, y_neg]
                    stop = [self.x + self.width + 10, y_neg]
                    self.screen.draw_line(self.axis_color, start, stop, self.axis_width)
                    if(axis_text):
                        x = self.x + self.width + 20
                        self.screen.draw_text(str(counter), [x, y_pos], self.font_color, 0)
                        self.screen.draw_text(str(-1 * counter), [x, y_neg], self.font_color, 0)
                    counter += step            
        else:
            counter = self.y #started from the bottom now we here
            step = self.height/float(self.num_x_axis+1)  #use floats boy!
            for l in range(self.num_x_axis):
                counter += step
                y = int(counter)
                start = [self.x, y]
                stop = [self.x + self.width + 10, y]
                self.screen.draw_line(self.axis_color, start, stop, self.axis_width)

    def find_scale(self, max_value, num_of_sections):
        start = 1.0
        if(max_value > start):
            #go up
            while(max_value > start * num_of_sections):
                start *= 2.0 #multiply by 2
            start /= 2.0
            
        elif(max_value <= start):
            #go down
            while(max_value < start * num_of_sections):
                start /= 2.0 #divide by two
            start *= 2.0
        return start #this will hold the
        

    def set_y_shift(self, value):
        self._shift = value + self.y

    def set_zoom(self, zoom):
        self.x_zoom = zoom


    def draw_charts(self):
        self.scale_charts(self.x_zoom)
        for i in range(len(self.scaled_chart_data)):
            color = self.charts[i].get_color()
            width = self.charts[i].get_width()
            try:
                self.screen.draw_lines(color, self.scaled_chart_data[i], width)
            except ValueError:
                #Chart is out of drawing range
                print ("Window Error: draw_charts() ValueError")
                pass
                
    def get_charts_max(self):
        max_y = 0
        max_x = 0
        for chart in self.charts:
            x, y = chart.get_max_values(self.width)
            if(max_y < y):
                max_y = y
                self.last_label = chart.get_last_label()
            if(max_x < x):
                max_x = x
        self.max_y = max_y
        self.max_x = max_x
        

    def draw_borders(self):
        self.screen.draw_rectangle(self.border_color, self.rect, self.border_width)

    def draw(self):
        self.get_charts_max()
        self.draw_charts()
        self.draw_x_axis()
        self.draw_y_axis()
        self.draw_borders()
    

    def add_chart(self, chart):
        self.charts.append(chart)

    def scale_charts(self, x_scale=1):
        """
        Scale charts
        """
        #self.get_charts_max()
        self.scaled_chart_data = []
        for chart in self.charts:
            #Scale in both the x and y direction
            #max_y = chart.get_max_y(self.width)

            points = []
            data = chart.get_rightmost_data(self.width/x_scale, self.max_x)
            for point in data:
                # Y scaling + Shifting
                try:
                    y = ((-1 * (point[1]/float(self.max_y))) * (self.height/2) + self.y_shift)
                except ZeroDivisionError:
                    y = ((-1 * (point[1]/1.0)) * (self.height/2) + self.y_shift)
                    


                # X Scaling + Shifting
                x = self.width - ((self.max_x - point[0]) * x_scale) + self.x

                # Save Point
                points.append([x, y])
            self.scaled_chart_data.append(points)
            
