from __future__ import absolute_import, print_function, unicode_literals


class ChatBotCore:
    """ ChatBotCore class is base class to inherit from to create new bots """
    def __init__(self, name='ChatBot', command_delimiter='/'):
        self.name = name
        self.command_delimiter = command_delimiter

    def _parse_command_message(self, message):
        """ Extract command name and arg string to pass to command """
        components = message.split()
        command = components[0]
        command = command.replace(self.command_delimiter, '', 1)
        args_string = ' '.join(comp for comp in components[1:] if comp)
        return (command, args_string)

    def _parse(self, user, message):
        """ Parse incoming message and call proper method for further actions """
        if message.startswith(self.command_delimiter):
            command, args_string = self._parse_command_message(message)
            return self._command(user, command, args_string)
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
