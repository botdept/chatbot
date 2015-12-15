from __future__ import absolute_import, print_function, unicode_literals


class ChatBotCore:
    """ ChatBotCore class is base class to inherit from to create new bots """
    def __init__(self):
        pass

    def notify(self, user, notification):
        """ Send notification to user
        notification is not a response to user message
        """
        pass

    def reply(self, user, message):
        """ Send reply message to user
        send reply for user free text message (as opposed to command message)
        """
        pass

    def process(self, user, message):
        """ Process user command message
        process user command message and optionally reply
        """
        pass
