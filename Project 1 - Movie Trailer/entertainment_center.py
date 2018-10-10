import fresh_tomatoes
import media

'''
Movie format:

movie_title = media.Movie(
    'movie title',
    'movie rating',
    'movie description',
    'movie poster link',
    'movie trailer link')

'''

the_shape_of_water = media.Movie(
    "The Shape of Water",
    "R",
    "At a top secret research facility in the 1960s, a lonely janitor forms a unique relationship with an amphibious creature that is being held in captivity. ",  # noqa
    "http://bit.ly/2FsV0kU",
    "https://www.youtube.com/watch?v=XFYWazblaUA")

avatar = media.Movie(
    "Avatar",
    "PG-13",
    "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",  # noqa
    "http://bit.ly/2oNa2bc",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

interstellar = media.Movie(
    "Interstellar",
    "PG-13",
    "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",  # noqa
    "http://bit.ly/2vGhZU4",
    "https://www.youtube.com/watch?v=ePbKGoIGAXY")

school_of_rock = media.Movie(
    "School of Rock",
    "PG",
    "An unlikely rock fanatic takes a shot at teaching it to young school students.",  # noqa
    "http://bit.ly/2Fta2Xj",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille",
    "G",
    "A rat finds himself behind the scenes with an unlikely to be chef",  # noqa
    "http://bit.ly/2oPHWfn",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie(
    "Hunger Games",
    "PG-13",
    "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",  # noqa
    "http://bit.ly/2oYosnM",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")


# add given Movie()s to array
movies = [
    the_shape_of_water,
    avatar,
    interstellar,
    school_of_rock,
    ratatouille,
    hunger_games]

# Use 'movies' array to pass data to fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
