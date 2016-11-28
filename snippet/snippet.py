class Snippet:
    def __init__(self, title, tag, text, user='$user', tech='$tech'):
        self.user = user
        self.title = title
        self.tag = tag
        self.text = text
        self.tech = tech

    def get_snippet(self):
        self.text = self.text.replace('$user', str(self.user))
        self.text = self.text.replace('$tech', str(self.tech))

        return [self.title, self.text]

    def get_snippet_text(self):
        self.text = self.text.replace('$user', str(self.user))
        self.text = self.text.replace('$tech', str(self.tech))

        return self.text

    def __str__(self):
        title, text = self.get_snippet()
        return '-' * 80 + '\n' + title + '-' * 80 + '\n' + text

