

def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

def snake_to_camel(word):
        """converts snake case string to camel case string"""
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))


