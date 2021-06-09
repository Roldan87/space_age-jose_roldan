from typing import AsyncGenerator

class SpaceAge:

    def __init__(self, user_age):
        # COACHES' NOTE: why use both user_age and seconds? user age is redundant and opaque, since the unit of measurement is not clear from the name.
        self.user_age = user_age
        # COACHES' NOTE: these are not sec(onds), these are years. a separate function to_years() would improve readability, that number looks hella ugly.
        self.earth_sec = self.user_age / 31557600
        self.seconds = user_age

    def on_earth(self):
        age_years = self.earth_sec
        return round(age_years, 2)
    
    def on_mercury(self):
        # COACHES' NOTE: a magic number like this is best assigned to a variable first e.g. conversion_factor
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

# COACHES' NOTE: Be careful of abbreviations, or even worse, wrong variable naming (seconds and years mean somthing very different).
