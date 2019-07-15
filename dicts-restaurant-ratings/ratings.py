"""Restaurant rating lister."""

def print_restaurant_rating():

    scores_file = open("scores.txt")
    rating_dict = {}

    for line in scores_file:
        line = line.rstrip().split(":")
        # line = tuple(line)

        rating_dict[line[0]] = line[1]

    # print(rating_dict)   

    input_restaurant = input("Enter the name of a restaurant > ")


    while True:

        input_rating = int(input("Enter rating > "))
        # print(input_rating)

        if input_rating >= 1 and input_rating <= 5:

            rating_dict[input_restaurant] = input_rating

            rating_dict = sorted(rating_dict.items()) 
            # print(rating_dict)


            for restaurant in rating_dict:
                print(f"{restaurant[0]} has a rating of {restaurant[1]}!")

            break

        else:
            print("Please enter a rating between 1 and 5.")

    scores_file.close()


