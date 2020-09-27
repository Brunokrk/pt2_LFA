class Word():
    """Palavra á aceitar ou rejeitar"""
    def __init__(self, word):
        self.word = word
        self.size = len(self.word)

    def __len__(self):
        return len(self.word)