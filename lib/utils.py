import random
import re

def generate_object_uuid() -> str:
    def replace_char(c):
        r = random.randint(0, 15)
        v = r if c == 'x' else (r & 0x3) | 0x8
        return format(v, 'x')

    return re.sub(r'[xy]', lambda match: replace_char(match.group(0)), 'xxxxxx-yxxxxx-8xxy-yx-xxxx-xxxxxxxxxxxx')