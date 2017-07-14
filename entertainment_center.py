#import media file containing movie data structure
import media
import fresh_tomatoes
#movie objects for 6 movies are created
avatar=media.Movie('Avatar','An alien adventure by a human.','img/avatar.jpg','https://www.youtube.com/watch?v=cRdxXPV9GNQ')
silence_lambs=media.Movie('Silence of the lambs','A thriller','img/silence.jpg','https://www.youtube.com/watch?v=RuX2MQeb8UM')
momento=media.Movie('Memento','A confusing suspense thriller','img/memento.jpg','https://www.youtube.com/watch?v=E77LfnMI-34')
raw=media.Movie('Raw','Seems like a good movie not watched yet','img/raw.jpg','https://www.youtube.com/watch?v=fHLJ7TH4ybw')
spiderman=media.Movie('Spiderman Homecoming','spiderman is coming back home..','img/spiderman-homecoming.jpg','https://www.youtube.com/watch?v=39udgGPyYMg')
la=media.Movie('L.A Confidential','if you havent watched it yet....pls watch','img/la.jpg','https://www.youtube.com/watch?v=C4XbnrmbEME')
#append list of movie objects
movie=[avatar,silence_lambs,momento,raw,spiderman,la]
#movie list is passed on to open_movies_page function
fresh_tomatoes.open_movies_page(movie)
