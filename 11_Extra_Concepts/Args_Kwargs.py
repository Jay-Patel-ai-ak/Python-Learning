# Find avg score using *args 

def average_score(*scores):
    if len(scores) == 0:
        return 0
    total = sum(scores) / len(scores)
    return total

print(average_score(90, 80, 70))  # Output: 80.0
print(average_score())  # Output: 0

# write a function describe_pet that accepts pet’s name & its required arguments

def describe_pet(name, animal_type, **details):
    print(f"{name} is a {animal_type}.")
    for key, value in details.items():
        print(f"{key}: {value}")   
    
describe_pet("Buddy", "dog", age=5, color="brown", favorite_food="bones")

# Write a fun make_sandwich that accepts any number of ingredients and prints them out.

def make_sandwich(*ingredients, **options):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
        
    print("Additional options:")
    for key, value in options.items():
        print(f"{key}: {value}")
   
# combines both *args and **kwargs        
make_sandwich("bread", "ham", "cheese", "lettuce", "tomato", size="large", toasted=True, sauce="mayo")

