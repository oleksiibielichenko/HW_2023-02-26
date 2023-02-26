user = {
    "name": "John",
    "age": 23,
    "friends": ["Mike", "Bob", "Joe"],
    "skills": ("HTML", "CSS", "JS"),
}

# 1) Find Mike into the user , than if u found Mike create a variable for him
print(user)
Mike = user["friends"][0]
# 2) Print Mike at the console
print("John has friend: ", Mike)
# 3) Get age of user , and guess when he was born
Age_of_user = user["age"]
print("John was born in: ", 2023 - Age_of_user)
# 4) Skills must look as : Python , QA , Selenium
user.update([("skills", ["Python" , "QA" , "Selenium"])])
print("Updated John's skills: ", user)
# 5) Sort john's friends

# 6) After sort find index position of "Bob"

# 7) Add new friends to friends : "Taras" , "Danya" , "Bidden"

# 8) Show how much skills user has