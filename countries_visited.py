"""
For this assignment, you must write a program that will:
Ask the user whether they want to enter a new country or quit.
If they want to enter a country, ask for the country name and add it to a list of countries.
Ask the user again whether they want to enter a new country, see their countries, or quit.
If they want to see their countries, show them the contents of their list in a nice format (i.e. don't just print the variable out!).
As an optional extra, you can also ask the user for when they visited the country, as well as the country name. That'll make the app a little more useful!
"""

my_list_of_countries = list()
country_name = str()
user_input = str()
option_is_valid = bool()

# Loop to control input from user, we want an 'a' or 'q'
while option_is_valid != True:
    user_input = input('\nDo you want to add a new country (a) or quit (q)? ')
    option_is_valid = user_input == 'a' or user_input == 'q'

# If we get a 'q' we skip loop and quit, if we choose 'a' we continue
# If we 'a' then we can select a new option 's'
while user_input != 'q':

    # Add details of country to list
    if user_input == 'a':
        country_name = str(input('Enter new country name: '))
        country_last_visited = str(input('When did you last visited it? '))
        my_list_of_countries.append({'name': country_name, 'last_visit': country_last_visited})

    # See list of countries
    elif user_input == 's':
        if len(my_list_of_countries) == 0:
            print("\nNot so fast, first add your first country!")
        else:
            for c in my_list_of_countries:
                print('- {} was last visited {}.'.format(c['name'], c['last_visit']))

    # After the first run, we will show an extended option (s)
    user_input = input('\nDo you want to add a new country (a), see your countries (s) or quit (q)? ')
