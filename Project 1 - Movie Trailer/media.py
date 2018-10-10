import webbrowser


class Movie():
    '''
    The Movies() class acts as a blueprint for creating movies and various
    other attributes defined in __init__
    '''

    # Initialize instances
    def __init__(
        self,               # Required Self
        movie_title,        # Movie Title
        movie_rating,       # Movie Rating
        movie_storyline,    # Movie Storyline
        poster_image,       # Poster Image url
        trailer_youtube     # Youtube trailer url
    ):

        self.title = movie_title                    # Title of Movie
        self.rating = movie_rating                  # Rating of movie
        self.storyline = movie_storyline            # Storyline of Movie
        self.poster_image_url = poster_image        # Poster Image
        self.trailer_youtube_url = trailer_youtube  # Youtube trailer link

    # Display trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
