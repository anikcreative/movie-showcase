# movie-showcase
### A Python-generated showcase that plays trailer videos for a set of movies. A project for the Udacity Full Stack Web Development Nanodegree.

### Important information
*entertainment_center.py* imports the *openpyxl* library, an external Python library (which can be found at https://openpyxl.readthedocs.io/en/default/) in order to read data from the cells within the *moviesdb.xlsx* spreadsheet.

### How it works
*entertainment_center.py* reads from an excel spreadsheet (*assets/moviesdb.xlsx*), aggregating a list of "Movie" objects (using the definition of the Movie object in *media.py*). This list of Movie objects, each object containing an attribute relating to the movie's title, director, rating, synopsis, and so on is then used to compile and write an HTML file, where each Movie object is represented in tile-like fashion inside a responsive page.

### Image assets
All box-art image assets are stored in the */assets/img* directory.
