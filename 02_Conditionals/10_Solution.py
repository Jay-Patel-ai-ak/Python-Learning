# 10. Pet Food Recommendation
# Recommend a type of pet food based on the pet's species and age. (e.g., Dog: < 2 years - Puppy food, Cat: > 5 years - Senior cat food).

pet_species = "Dog"
pet_age = 1  # in years 

if pet_species == "Dog":
    if pet_age < 2:
        food = "Puppy food"
    else:
        food = "Adult dog food"
elif pet_species == "Cat":
    if pet_age > 5:
        food = "Senior cat food"
    else:
        food = "Adult cat food"
else:
    food = "Please specify a valid pet species (Dog or Cat)."
    
print(f"For a {pet_age}-year-old {pet_species}, we recommend: {food}")