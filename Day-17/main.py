# class User:
#     pass
#
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "cipher"
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "chuck"
# print(user_2.username)

# This is also an easier way to do this

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001", "cipher")
user_2 = User("002", "Henry cavill")
# print(user_2.username)
# print(user_2.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
