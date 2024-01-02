class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.contacts = []

    def add_contact(self, user):
        print(f"Adding {[contact.username for contact in user.contacts]} to {self.username}'s contacts")
        self.contacts.append(user)

    def send_message(self, recipient, content):
        if recipient in self.contacts:
            message = Message(self, recipient, content)
            recipient.receive_message(message)
        else:
            print(f"Error: {recipient.username} not in contacts list. Cannot send message.")

    def receive_message(self, message):
        print(f"Received message from {message.sender.username}: {message.content}")

class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content

class GroupChat(Message):
    def __init__(self, sender, recipients, content):
        super().__init__(sender, None, content)
        self.recipients = recipients

    def add_member(self, user):
        if user not in self.recipients:
            self.recipients.append(user)
            print(f"Added {user.username} to the group chat.")
        else:
            print(f"{user.username} is already a member of the group chat.")

# Example Usage:
user1 = User('user1', 'user1@example.com')
user2 = User('user2', 'user2@example.com')
user3 = User('user3', 'user3@example.com')

user1.send_message(user3, 'Hello!')
user1.send_message(user2, 'Hello!')

group_chat = GroupChat(user1, [user2, user3], 'Group chat message')
group_chat.add_member(user1)
group_chat.add_member(user2)
