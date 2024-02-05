def get_movie_recommendation(genre, rating):

if genre.lower() == "action" and rating > 8:

return "We recommend an action blockbuster."

elif genre.lower() == "comedy" or rating > 7:

return "We recommend a funny movie."

elif genre.lower() != "romance" and rating < 6:

return "We recommend a thriller."

else:

return "We recommend a general audience movie."

def main():

print("Welcome to the Movie Recommender!")

user_genre = input("What movie genre do you prefer?")

user_rating = float(input("What's the minimum movie rating you would consider (1-10)?"))

recommendation = get_movie_recommendation(user_genre, user_rating)

print(recommendation)

if _name_ == "_main_":

main()
