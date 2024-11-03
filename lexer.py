import re

TOKEN_SPECIFICATION = [
    ('COMMENT', r'//.*'),
    ('KEYWORD', r'\b(?:int|float|char|if|else|for|while|return|void|switch|case|break|continue|default|do|typedef|struct|union|enum|const|sizeof|unsigned)\b'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('NUMBER', r'\b\d+(\.\d*)?([eE][+-]?\d+)?\b'),
    ('OPERATOR', r'[+\-*/%=&|<>!]=?|&&|\|\|'),
    ('SEPARATOR', r'[{}()\[\],;<>]'),        
    ('STRING', r'"(\\.|[^"\\])*"'),
    ('CHAR', r"\'(\\.|[^'\\])\'"),
    ('PREPROCESSOR', r'#\s*(?:include|define)\b.*'),
    ('WHITESPACE', r'\s+'),
    ('MISMATCH', r'.'),
]

token_re = re.compile(
    '|'.join(
        f'(?P<{name}>{pattern})'
        for name, pattern in TOKEN_SPECIFICATION
    )
)

def lex(code):
    tokens = []
    for match in token_re.finditer(code):
        kind = match.lastgroup
        value = match.group(kind)
        if kind == 'WHITESPACE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value} at position {match.start()}')
        tokens.append((kind, value))
    return tokens
