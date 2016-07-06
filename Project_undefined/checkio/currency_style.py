import re

def checkio(text):
    pattern = re.compile('(\$\d{1,3}((\.|\,)(\d{1,3}))*)')
    def replacement(match):
        whole_match = match.group(0)
        if len(whole_match) > 2:
            if whole_match[-3] == ',' or whole_match[-4] == '.':
                return whole_match.replace(',', '%temp%').replace('.', ',').replace('%temp%', '.')
            else:
                return whole_match
        else:
            return whole_match
    
    return (re.sub(pattern, replacement, text))
