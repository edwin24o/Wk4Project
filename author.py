class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def get_details(self):
        return f"Name: {self.name}, Biography: {self.biography}"