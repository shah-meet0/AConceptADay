from datetime import datetime


class Post:

    def __init__(self, author, title, content, category):
        self.time_created = datetime.now()
        self.author = author
        self.title = title
        self.content = content # In Markdown format
        self.category = category

    def save(self):
        pass  # to ./posts in a way that streamlit can import it

    def import_from_word(self, filepath):
        pass


