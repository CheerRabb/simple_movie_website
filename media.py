# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.


class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movie_title, movie_release_date, movie_starring, movie_poster, movie_trailer):
        # initialize instance of class Movie
        self.title = movie_title
        self.release_date = movie_release_date
        self.starring = movie_starring
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
