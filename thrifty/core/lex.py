"""
Lexer / tokenizer for thrift files
"""
import ply.lex as lex

keywords = (
    'namespace',
    'void', 'async',
    'bool', 'byte', 'binary',
    'i16', 'i32', 'i64', 'double',
    'map', 'list', 'set',
    'struct', 'exception',
    'service', 'extends', 'throws',
    'typedef', 'enum', 'const',
    'required', 'optional',
)

reserved = (
    'abstract', 'and', 'args', 'as', 'assert', 'break',
    'case', 'class', 'continue', 'declare', 'def', 'default',
    'del', 'delete', 'do', 'elif', 'else', 'elseif', 
    'except', 'exec', 'false', 'finally', 'float', 'for',
    'foreach', 'function', 'global', 'goto', 'if', 'implements',
    'import', 'in', 'inline', 'instanceof', 'interface', 'is',
    'lambda', 'native', 'new', 'not', 'or', 'pass',
    'public', 'print', 'protected', 'raise', 'return', 'sizeof',
    'static', 'switch', 'synchronized', 'this', 'throw', 'transient',
    'true', 'try', 'unsigned', 'var', 'virtual', 'volatile',
    'while', 'with', 'union', 'yield',
)

tokens = keywords + reserved + (
    'COMMA', 'INTEGER', 'FLOAT', 'HEX', 'STRING', 'SYMBOL',
    'IDENTIFIER', 'SILLYCOMM', 'MULTICOMM', 'UNIXCOMMENT',
    'NEWLINE',
)

t_ignore = ' \t'

t_COMMA      = r'\,'
t_INTEGER    = r'[+-]?[0-9]+'
t_FLOAT      = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_HEX        = r'"0x"[0-9A-Fa-f]+'
t_STRING     = r'\".*?\"'
t_SYMBOL     = r'[:;\,\{\}\(\)\=<>\[\]]'
t_IDENTIFIER = r'[a-zA-Z_][\.a-zA-Z_0-9]*'


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t


def t_error(t):
    print('Illegal character %s' % t.value[0])
    t.lexer.skip(1)


def tokenize(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: break
        print tok


lexer = lex.lex()
