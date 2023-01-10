# Token types

INTEGER_CONST = 'INTEGER_CONST'
PLUS          = 'PLUS'
MINUS         = 'MINUS'
MULTIPLY      = 'MULTIPLY'
REGISTER      = 'REGISTER'
COMMAND       = 'COMMAND'
COLON         = 'COLON'
IF_OPERATOR   = 'IF_OPERATOR'
LET_COMMAND   = 'LET'
IF_COMMAND    = 'IF'
JUMP_COMMAND  = 'JUMP'
CALL_COMMAND  = 'CALL'
RETURN_COMMAND = 'RETURN'
PRINT_COMMAND = 'PRINT'
LABEL         = 'LABEL'
GOTO_LABEL    = 'GOTO_LABEL'
ASSIGN        = 'ASSIGN'
OPERATOR      = 'OPERATOR'
EQUAL_TO      = 'EQUAL_TO'
LESS_THEN     = 'LESS_THEN'
GREATER_THEN  = 'GREATER_THEN'
EXPRESSION    = 'EXPRESSION'
EOL           = 'EOL'
END           = 'END'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"

    def __repr__(self):
        return self.__str__()


RESERVED_COMMANDS = {
    'LET': Token(COMMAND, 'LET'),
    'IF': Token(COMMAND, 'IF'),
    'JUMP': Token(COMMAND, 'JUMP'),
    'CALL': Token(COMMAND, 'CALL'),
    'RETURN': Token(COMMAND, 'RETURN'),
    'PRINT': Token(COMMAND, 'PRINT'),
}