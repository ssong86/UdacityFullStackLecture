import media

'''toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=SgoiKLFBA3Q")

print(toy_story.storyline)

# self = toy_story
# movie_title = Toy Story
# and so on

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v==9ceBgWV8io")
print(avatar.storyline)
avatar.show_trailer()

# avatar = media.Movie()
# objectname = library.classname
'''
'''
#for quiz
spider_man = media.Movie("Spiderman",
                         "Spiderman hero movie who has super power of a spider",
                         "https://en.wikipedia.org/wiki/Spider-Man#/media/File:Web_of_Spider-Man_Vol_1_129-1.png",
                         "https://www.youtube.com/watch?v=xEvV3OsE2WM")
spider_man.show_trailer()'''
#for mini project
import fresh_tomatoes

spider_man1 = media.Movie("Spider Man 1", "A story of spider man, first film",
                          "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
                          "https://www.youtube.com/watch?v=fqYHg-Ue_Cc")
spider_man2 = media.Movie("Spider Man 2", "A story of spider man, second film",
                          "https://upload.wikimedia.org/wikipedia/en/0/02/Spider-Man_2_Poster.jpg",
                          "https://www.youtube.com/watch?v=enmFqm_N_ZE")
spider_man3 = media.Movie("Spider Man 3", "A story of spider man, third",
                          "https://upload.wikimedia.org/wikipedia/en/7/7a/Spider-Man_3%2C_International_Poster.jpg",
                          "https://www.youtube.com/watch?v=PCmMLfXdURs")
spider_man_reboot1 = media.Movie("Amazing Spider Man 1", "Reboot of spider man, first film",
                                 "https://upload.wikimedia.org/wikipedia/en/0/02/The_Amazing_Spider-Man_theatrical_poster.jpeg",
                                 "https://www.youtube.com/watch?v=uAcD7H53220")
spider_man_reboot2 = media.Movie("Amazing Spider Man 2", "Reboot of spider man, second film",
                                 "https://upload.wikimedia.org/wikipedia/en/0/02/The_Amazing_Spiderman_2_poster.jpg",
                                 "https://www.youtube.com/watch?v=DlM2CWNTQ84")
spider_man_homecoming = media.Movie("Spider Man: Homecoming", "New story of spider man",
                                    "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                                    "https://www.youtube.com/watch?v=U0D3AOldjMU")

my_movies = [spider_man1, spider_man2, spider_man3, spider_man_reboot1, spider_man_reboot2,
             spider_man_homecoming]
#fresh_tomatoes.open_movies_page(my_movies)
#print(media.Movie.VALID_RATINGS) # calling a class variable, valid_ratings
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
