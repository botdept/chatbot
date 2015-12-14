import unittest

from bot.core import ChatBot


class TestChatBot(unittest.TestCase):
    def setUp(self):
        self.chatbot = ChatBot()

    def test_command_message(self):
        """ Bot should be able to respond to certain command messages """
        self.assertTrue(hasattr(self.chatbot, 'reply'))

    def test_free_text_message(self):
        """ Bot should be able to respond to any free text message """
        self.assertTrue(hasattr(self.chatbot, 'process'))

    def test_notification_message(self):
        """ Bot should be able to respond to any free text message """
        self.assertTrue(hasattr(self.chatbot, 'notify'))
