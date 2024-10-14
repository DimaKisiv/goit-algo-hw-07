class Comment:
    def __init__(self, message, user):
        self.message = message
        self.user = user
        self.is_deleted  = False
        self.replies = []

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.message = "Цей коментар було видалено."
        self.is_deleted  = True

    def display(self, level=0):
        space = "    " * level
        display_text = f"{space}{self.message}" if self.is_deleted else f"{space}{self.user}: {self.message}" 
        print(display_text)
        for reply in self.replies:
            reply.display(level + 1)


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()