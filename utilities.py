from datetime import datetime
from datetime import timezone
import pickle

class Post:

    def __init__(self, author, title, content, category):
        self.time_created = datetime.now(tz=timezone.utc)
        self.author = author
        self.title = title
        self.content = content # In Markdown format
        self.category = category

    def save(self):
        with open(f'./posts/{self.title.lower()}.pkl', 'wb') as p:
            pickle.dump(self, p)

    def import_from_word(self, filepath):
        pass

    def __str__(self):
        return (f'#H1 {self.title} \n' +
                f'#H2 {self.time_created.strftime("%a %d %b %Y %I:%M %p")} \n' +
                self.content)


def parse_post(post_file):
    return pickle.load(post_file)
