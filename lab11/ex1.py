class Cylinder:
    def __init__(self,radius,height):
        self.set_radius(radius)
        self.set_height(height)

    def get_radius(self):
        return self.radius
    def set_radius(self,radius):
        if radius>0:
            self.radius = radius
    def get_height(self):
        return self.height
    def set_height(self,height):
        if height>0:
            self.height = height

    def calc_base_area(self):
        return 3.14 * (self.radius**2)
    def calc_surface_area(self):
        return 2 * (3.14 * self.radius) * self.height

    def calc_area(self):
        return 2 * self.calc_base_area() + self.calc_surface_area()

    def calc_volume(self):
        return self.calc_base_area() * self.height

cylinder = Cylinder(3,5)
print ("Area:",cylinder.calc_area())
print ("Volume:",cylinder.calc_volume())