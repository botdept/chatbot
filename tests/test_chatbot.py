import unittest
import mock

from bot.core import ChatBotCore


class TestChatBot(unittest.TestCase):
    def setUp(self):
        self.chatbot = ChatBotCore()

    def test_chatbot_name(self):
        """ Bot can have name """
        name = 'test_name'
        cb = ChatBotCore(name)
        self.assertEqual(name, cb.name)

    def test__parse(self):
        """ _parse method should return proper function and arguments for it
        by default if message starts with / - it's command message
        otherwise it's free text message
        """
        command = '/command'
        self.chatbot._command = mock.Mock()
        self.chatbot._parse(None, command)
        self.chatbot._command.assert_called_once_with(None, command[1:])

        free_text = 'message'
        self.chatbot._free_text = mock.Mock()
        self.chatbot._parse(None, free_text)
        self.chatbot._free_text.assert_called_once_with(None, free_text)

    def test__parse_command_message(self):
        """ _parse_command_message should return command name and arguments for the command if required """
        command = 'command'
        cmd1 = '/{}'.format(command)
        cmd2 = '/{} 1'.format(command)
        cmd3 = '/{} 1   2 3'.format(command)
        self.assertEqual((command, ()), self.chatbot._parse_command_message(cmd1))
        self.assertEqual((command, ('1',)), self.chatbot._parse_command_message(cmd2))
        self.assertEqual((command, ('1', '2', '3')), self.chatbot._parse_command_message(cmd3))

    def test_command_message(self):
        """ Bot should be able to respond to certain command messages """
        self.assertTrue(hasattr(self.chatbot, '_command'))

    def test_free_text_message(self):
        """ Bot should be able to respond to any free text message """
        self.assertTrue(hasattr(self.chatbot, '_free_text'))

    def test_notification_message(self):
        """ Bot should be able to respond to any free text message """
        self.assertTrue(hasattr(self.chatbot, 'notify'))
