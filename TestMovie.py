import movie
import fresh_tomatoes
avatar=movie.Movie('Avatar','An alien adventure by a human.','img/avatar.jpg','https://www.youtube.com/watch?v=cRdxXPV9GNQ')
silence_lambs=movie.Movie('Silence of the lambs','A thriller','img/silence-of-the-lambs.jpg','https://www.youtube.com/watch?v=RuX2MQeb8UM')
momento=movie.Movie('Memento','A confusing suspense thriller','img/memento.jpg','https://www.youtube.com/watch?v=E77LfnMI-34')
raw=movie.Movie('Raw','Seems like a good movie not watched yet','img/raw.jpg','https://www.youtube.com/watch?v=fHLJ7TH4ybw')
spiderman=movie.Movie('Spiderman Homecoming','spiderman is coming back home...When did he leave','img/spiderman-homecoming.jpg','https://www.youtube.com/watch?v=39udgGPyYMg')
la=movie.Movie('L.A Confidential','if you havent watched it yet....pls watch','img/la.jpg','https://www.youtube.com/watch?v=C4XbnrmbEME')
##print(avatar.storyline)

#avatar.movie_trailer()

movie=[avatar,silence_lambs,momento,raw,spiderman,la]
fresh_tomatoes.open_movies_page(movie)
print(movie.Movie.__name__)
