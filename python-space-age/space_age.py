from typing import AsyncGenerator


class SpaceAge:

    def __init__(self, user_age):
        self.user_age = user_age
        self.earth_sec = self.user_age / 31557600
        self.seconds = user_age

    def on_earth(self):
        age_years = self.earth_sec
        return round(age_years, 2)
    
    def on_mercury(self):
        age_years = self.earth_sec / 0.2408467
        return round(age_years, 2)

    def on_venus(self):
        age_years = self.earth_sec / 0.61519726
        return round(age_years, 2)

    def on_mars(self):
        age_years = self.earth_sec / 1.8808158
        return round(age_years, 2)

    def on_jupiter(self):
        age_years = self.earth_sec / 11.862615
        return round(age_years, 2)

    def on_saturn(self):
        age_years = self.earth_sec / 29.447498
        return round(age_years, 2)

    def on_uranus(self):
        age_years = self.earth_sec / 84.016846
        return round(age_years, 2)

    def on_neptune(self):
        age_years = self.earth_sec / 164.79132
        return round(age_years, 2)