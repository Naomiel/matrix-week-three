# Import all required modules

from unittest import TestCase


class EmailParser(TestCase):
    def setUp(self):
        self.email_parser = EmailParser()

    def test_parse_valid_email(self):
        email = 'johndoe@gmail.com'
        expected_output = {'username': 'johndoe', 'domain': 'gmail.com'}
        parsed_email = self.email_parser.parse(email)
        self.assertEqual(parsed_email, expected_output)

    def test_parse_invalid_email(self):
        email = 'johndoe@invalid'
        parsed_email = self.email_parser.parse(email)
        self.assertIsNone(parsed_email)

    def test_convert_to_dict(self):
        values = ['johndoe', 'gmail.com']
        expected_output = {'username': 'johndoe', 'domain': 'gmail.com'}
        converted_dict = self.email_parser.convert_to_dict(values, self.email_parser.keys)
        self.assertEqual(converted_dict, expected_output)

if __name__ == '__main__':
    TestCase.main()