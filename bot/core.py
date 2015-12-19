from __future__ import absolute_import, print_function, unicode_literals


class ChatBotCore:
    """ ChatBotCore class is base class to inherit from to create new bots """
    def __init__(self, name='ChatBot'):
        self.name = name

    def _parse_command_message(self, message):
        components = message.split()
        command = components[0][1:]
        args = tuple(cmp for cmp in components[1:] if cmp)
        return (command, args)

    def _parse(self, user, message):
        """ Parse incoming message and call proper method for further actions """
        if message.startswith('/'):
            command, args = self._parse_command_message(message)
            return self._command(user, command, *args)
        else:
            return self._free_text(user, message)

    def notify(self, user, notification):
        """ Send notification to user
        notification is not a response to user message
        """
        pass

    def _free_text(self, user, message):
        """ Send reply message to user
        send reply for user free text message (as opposed to command message)
        """
        pass

    def _command(self, user, command, *args):
        """ Process user command message
        process user command message and optionally reply
        """
        pass

    def _send_message(self, user, message):
        pass
