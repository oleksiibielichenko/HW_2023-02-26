user = {
    "name": "John",
    "age": 23,
    "friends": ["Mike", "Bob", "Joe"],
    "skills": ("HTML", "CSS", "JS"),
}
# 1) Find Mike into the user , than if u found Mike create a variable for him
print("1) User: ",user)
Mike = user["friends"][0]
# 2) Print Mike at the console
print("2) John has friend: ", Mike)
# 3) Get age of user , and guess when he was born
Age_of_user = user["age"]
print("3) John was born in: ", 2023 - Age_of_user)
# 4) Skills must look as : Python , QA , Selenium
user.update([("skills", ["Python" , "QA" , "Selenium"])])
print("4) Updated John's skills: ", user)
# 5) Sort john's friends
friends = user.get("friends")
friends.sort()
user.update([("friends", friends)])
print("5) Sorted John's friends: ", user)
# 6) After sort find index position of "Bob"
index = friends.index("Bob")
print("6) Index of Bob: ",index)
# 7) Add new friends to friends : "Taras" , "Danya" , "Bidden"
friends.append("Taras")
friends.append("Danya")
friends.append("Bidden")
user.update([("friends", friends)])
print("7) Add friends to John: ", user)
# 8) Show how much skills user has
