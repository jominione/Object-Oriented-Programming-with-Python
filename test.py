class Car:

    def __init__(self, model, year, colour):
        self.model = model
        self.year = year
        self.colour = colour
        self.speed = 0
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour):
        if not isinstance(colour, str):
            raise TypeError('Colour must be a string')

        self._colour = colour

# Examples:

ferrari = Car('Ferrari', 2024, 'Red')
print(ferrari.model)
print(ferrari.year)
print(ferrari.colour)

ferrari.colour = 'Blue'

print(ferrari.colour)