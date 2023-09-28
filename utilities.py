from datetime import datetime
import pickle
import mammoth
import pandoc
import os
from zoneinfo import ZoneInfo
import shutil
class Post:

    def __init__(self, author, title, content, category):
        self.time_created = datetime.now(ZoneInfo('Europe/London'))
        self.author = author
        self.title = title
        self.content = content # In Markdown format
        self.category = category

    def save(self):
        with open(f'./posts/{self.title.lower()}.pkl', 'wb') as p:
            pickle.dump(self, p)

    def export_to_word(self):
        filepath = f'./word_files/{self.title.lower()}.docx'
        with open(filepath, 'wb') as wf:
            pandoc.write(pandoc.read(self.content), file=wf, format='docx')
        return filepath

    def export_to_word_and_save(self):
        filepath = self.export_to_word()
        os.startfile(os.path.normpath(filepath)) # For some reason os isn't just able to read the path
        input('Press Enter when done editing')
        import_from_word(filepath, self.title, self.category, self.author)
        print('Edited and Saved')

    def __str__(self):
        return (f'### {self.title} \n' +
                f'###### {self.time_created.strftime("%a %d %b %Y %I:%M %p")} \n' +
                self.content)


def parse_post(filepath):
    with open(filepath, 'rb') as f:
        parsed_post = pickle.load(f)
    return parsed_post


def import_from_word(filepath, title, category, author='Meet Shah'):
    with open(filepath, 'rb') as docx_file:
        content_in_markdown = mammoth.convert_to_markdown(docx_file).value
        converted_contents = pandoc.write(pandoc.read(content_in_markdown), format='markdown')
    #     content_in_markdown = mammoth.convert_to_markdown(
    #         docx_file, convert_image=mammoth.images.img_element(ImageWriter(title, './assets/images/'))).value
    # converted_contents = pandoc.write(pandoc.read(content_in_markdown), format='markdown')

    imported_post = Post(author, title, converted_contents, category)
    imported_post.save()
    return imported_post


# Copied mostly from mammoth documentation with some additions
class ImageWriter(object):
    def __init__(self, prefix, output_dir):
        self._prefix = prefix
        self._output_dir = output_dir
        self._image_number = 1

    def __call__(self, element):
        extension = element.content_type.partition("/")[2]
        image_filename = "{0}_{1}.{2}".format(self._prefix, self._image_number, extension)
        with open(os.path.join(self._output_dir, image_filename), "wb") as image_dest:
            with element.open() as image_source:
                shutil.copyfileobj(image_source, image_dest)

        self._image_number += 1

        return {"src": self._output_dir + image_filename}





