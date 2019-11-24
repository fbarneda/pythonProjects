"""
Here’s the three main features:

First, the application must allow to add new movies to the collection;
The application must allow users to view all the movies in their collection;
The application must also allow users to find any particular movie by any of its attributes.

What are movies?

Movies will be dictionaries, but you can define the structure of the dictionary to be anything you like.
For example, you may choose to have movies as dictionaries with only three keys:

{
  'name': 'The Matrix',
  'director': 'Wachowskis',
  'year': '1994'
}

Or you may choose to have more keys (in the example below, also including which shelf and location the movie is in):

{
  'name': 'The Matrix',
  'director': 'Wachowskis',
  'year': '1994',
  'location': '3F-14',
  'shelf': '3F'
}
Where will movies be stored?
It’s up to you where movies will be stored, as long as you can then print them, retrieve them, and find them. A good potential structure could be a list. If you are familiar with files and storing things in files, go for that!

What's that about "finding movies"?
Once you have the movie structure defined, users should be able to e.g. “find all movies released in 1994”. Or, “find all movies by director Rolf Smith”.

That means the user must be able to tell you what property they are looking for (is it year, director, or something else); and also they must be able to tell you what they’re looking for (1994, or Rolf Smith in the examples above).

With both the property and the value, you’ll be able to find all movies which match both. It’s tricky! Spend some time, and I’m sure you’ll get it.
"""
movie_collection_db = list()
movie_collection_keys = ['name', 'director', 'year', 'location', 'shelf']

options_msg = """ 
- Add a Movie (a)
- View all your Movies (v)
- Search your Movies (s)
- Delete a Movie (d)
- Write all Changes (w)
- Quit (q)
"""


def add_single_movie_to_db():
    data = list()

    for key in movie_collection_keys:
        msg = "Enter movie {}: ".format(key)
        d = input(msg)
        data.append(d)

    movie_data = dict(zip(movie_collection_keys, data))
    movie_collection_db.append(movie_data)


def view_all_movie_db():
    if len(movie_collection_db) == 0:
        print("\nYou don't have any movies yet.\nTry again later.")
    else:
        for movie in movie_collection_db:
            print_movie_info(movie)


def print_movie_info(movie):
    print("* {} directed by {} in {}\nLocated in {}, shelf {}.\n".format(
        movie["name"],
        movie["director"],
        movie["year"],
        movie["location"],
        movie["shelf"]
    ))


def read_local_movie_db():
    try:
        with open("movie_db.txt", "r") as file:
            data = eval(file.read())
        return data

    except:
        return None


def write_all_changes(data):
    with open("movie_db.txt", "w") as file:
        file.writelines(str(data))


# Ask the customer to enter one of the options offered
print("Welcome to my Movie Management System!")
opt_selected = bool()

trying_to_read = read_local_movie_db()
if trying_to_read is not None:
    movie_collection_db = trying_to_read

print(type(trying_to_read))
print(trying_to_read)
print()
print(type(movie_collection_db))
print(movie_collection_db)


# if local_movie_db is not None:
#     for line in local_movie_db:
#         movie_collection_db.upd

# [
# {'name': '1', 'director': '1', 'year': '1', 'location': '1', 'shelf': '1'},
# {'name': '1', 'director': '1', 'year': '1', 'location': '1', 'shelf': '1'}
# ]

# example: [{'name': '1', 'director': '1', 'year': '1', 'location': '1', 'shelf': '1'}, {'name': '2', 'director': '2', 'year': '2', 'location': '2', 'shelf': '2'}, {'name': '3', 'director': '3', 'year': '3', 'location': '3', 'shelf': '3'}, {'name': '4', 'director': '4', 'year': '4', 'location': '4', 'shelf': '4'}]

while opt_selected != "q":

    print(movie_collection_db)

    print("Movie collection:" + options_msg)
    opt_selected = input("Select an option to continue\n" + "-" * 30 + "\n").lower()

    # Add a Movie (a)
    if opt_selected == "a":
        add_single_movie_to_db()
    # View all your Movies (v)
    elif opt_selected == "v":
        view_all_movie_db()
    # Search your Movies (s)
    elif opt_selected == "s":
        pass
    # Delete a Movie (d)
    elif opt_selected == "d":
        pass
    # Write all Changes (w)
    elif opt_selected == "w":
        write_all_changes(data=movie_collection_db)
    # Quit (q)
    elif opt_selected == "q":
        break
    else:
        print("\nInvalid option. Try again.")
        continue

print("\nBye now!")

# movie_collection = [{
#     'name': 'The Matrix',
#     'director': 'Wachowskis',
#     'year': '1994',
#     'location': '3F-14',
#     'shelf': '3F'
# }]
