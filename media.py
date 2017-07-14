import webbrowser
#movie data structure  containing title,storyline ,poster,trailer


class Movie():

    def __init__(self,movie_title,storyline,poster_img,youtube_trailer_url):
        self.title=movie_title
        self.storyline=storyline
        self.poster_image_url=poster_img
        self.trailer_youtube_url=youtube_trailer_url
#storyline is not used
