import webbrowser

_YT_PATH = "https://www.youtube.com/watch?v="
_IMG_PATH = "assets/img/"

# Movie class to define any movie objects
class Movie():
    """Class 'Movie': provides a definition for a Movie variable that stores information related to individual films."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NR"]

    def __init__(self,
                 _title,
                 _year,
                 _director,
                 _synopsis,
                 _image,
                 _trailer,
                 _stars,
                 _rating):
        global _IMG_PATH
        self.title      = _title
        self.year       = _year
        self.director   = _director
        self.synopsis   = _synopsis
        self.image      = _IMG_PATH + _image
        self.trailer    = _trailer
        self.stars      = _stars
        self.rating     = _rating

    def get_image(self):
        open(_IMG_PATH + self.image)

    def get_trailer(self):
        webbrowser.open(_YT_PATH + self.trailer)
