from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Initial knowledge"]

    def teach(self):
        return self.knowledge[0]