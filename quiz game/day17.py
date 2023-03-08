class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username



steve = User("001", "Steve")

print(steve.id)


