"""Restaurant rating lister."""

scores_file = open("scores.txt")
rating_dict = {}

for line in scores_file:
    line = line.rstrip().split(":")
    # line = tuple(line)

    rating_dict[line[0]] = line[1]

# print(rating_dict)   

rating_dict = sorted(rating_dict.items()) 
print(rating_dict)


for restaurant in rating_dict:
    print(f"{restaurant[0]} has a rating of {restaurant[1]}!")


close("scores.txt")
