
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
        self.border_color = (200,200,200)
        self.border_width = 2

    def set_y_shift(self, value):
        self._shift = value + self.y

    def set_zoom(self, zoom):
        self.x_zoom = zoom

    def draw_charts(self):
        self.scale_charts(self.x_zoom)
        for i in range(len(self.scaled_chart_data)):
            color = self.charts[i].get_color()
            width = self.charts[i].get_width()
            self.screen.draw_lines(color, self.scaled_chart_data[i], width)

    def draw_borders(self):
        self.screen.draw_rectangle(self.border_color, self.rect, self.border_width)

    def draw(self):
        self.draw_charts()
        self.draw_borders()
    

    def add_chart(self, chart):
        self.charts.append(chart)

    def scale_charts(self, x_scale=1):
        """
        Scale charts
        """
        max_y = 0
        self.scaled_chart_data = []
        for chart in self.charts:
            y = chart.get_max_y(self.width)
            if(max_y < y):
                max_y = y
        for chart in self.charts:
            #Scale in both the x and y direction
            #max_y = chart.get_max_y(self.width)

            points = []
            data = chart.get_rightmost_data(self.width/x_scale)
            for point in data:
                # Y scaling + Shifting
                try:
                    y = ((-1 * (point[1]/float(max_y))) * (self.height/2) + self.y_shift)
                except ZeroDivisionError:
                    y = ((-1 * (point[1]/1.0)) * (self.height/2) + self.y_shift)
                    


                # X Scaling + Shifting
                x = self.width - ((data[0][0] - point[0]) * x_scale) + self.x

                # Save Point
                points.append([x, y])
            self.scaled_chart_data.append(points)
            
