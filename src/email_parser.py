import re


class EmailParser:
    # regex pattern that validate email
    pattern = r'^([a-zA-Z][a-zA-Z0-9]*)@([a-zA-Z][a-zA-Z0-9]*\.com)$'

    keys = ['username', 'domain']

    def parse(self, email):
        ''' parse email and return a dictionary of username and domain if valid and return None otherwise'''
        match = re.match(self.regex_pattern, email)

        if match:
            username = match.group(1)
            domain = match.group(2)

            return {'username': username, 'domain': domain}
        
        return None


    def convert_to_dict(self, keys, values):
        '''
          Takes in two lists as params and return them as a dictionary.'''
        return dict(zip(keys, values))
