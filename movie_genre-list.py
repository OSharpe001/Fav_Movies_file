name=input("What's your name? ")  #ASK FOR THE USER'S NAME

def movieList(): #FUNCTION TO GET A LIST OF MOVIES AND GENRES FROM USER
    movie_dict={}   #START A FRESH, EMPTY DICTIONARY TO HOLD MOVIE GENRES AND TITLES
    genre_selection=input("List all genres you would like to have (seperated by commas): ")    # GIVE ME ALL THE GENRES AT ONCE
    genres=genre_selection.split(",")   #SPLIT ALL THE GIVEN GENRES INTO A LIST
    for genre in genres:  #ITERATE THROUGH THE LIST OF GENRES CALLED "genres"
        if genre[0]==" ":
            genre=genre[1:]
        movie_list=[]
        movies=(input(f"Give me a few movies for the genre {genre} (seperated by commas): ")) #GET A BUNCH OF MOVIES FOR THIS GENRE
        for movie in movies.split(','):
            if movie[0]==' ':
                movie=movie[1:]
            movie_list.append(movie)
        movie_dict[genre]=movie_list             
    print(f"\n\n{name}'s Movie List!\n--                      --")  #MAKE A TITLE FOR THE NEW MOVIE LIST WITH THE USER'S NAME
    return movie_dict   #SEND BACK THE INFORMATION TO THE VARIABLE 'my_list' TO SAVE THE NEW DICTIONARY

def make_movie_file(fname, info):
    with open(fname, 'w') as outfile:
        for genre in info:
            outfile.write(f"{genre}: {info[genre]}\n")


my_list=movieList() #"my_list" CALLS THE FUNCTION "movieList()" TO GET THE MOVIE INFO FROM THE USER
for genre in my_list: #SPLITTING UP THE INFO FROM THE DICTIONARY
    print(genre, my_list[genre]) #PRINT EVERY GENRE AND CORESPONDING MOVIES ON DIFFERENT LINES
print("")

make_movie_file((f"{name}'s_Movie_List"),my_list)

"""
SAMPLE INFO
-------------
Comedy, Romance, Thriller
Laugh All Day, Laugh All Night
Kiss/Kiss, The Huggers
Killer Killers, Run Them Down
"""