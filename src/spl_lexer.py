
from src.spl_token import *

class Lexer:
    def __init__(self, text):
        # text line
        self.text = text
        # self.pos is the index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.current_token = self.get_next_token()

    def __str__(self):
        return f"Text line: {self.text}, pos: {self.pos}, current_char: {repr(self.current_char)})"

    def __repr__(self):
        return self.__str__()

    # def error(self):
    #     raise Exception('Invalid character')

    def get_current_token(self):
        return self.current_token

    # def error(self):
    #     raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            raise Exception('Not token that was expected')

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable"""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            # indicates the end of input
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def peek(self):
        """Peek next position character"""
        peek_pos = self.pos + 1
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        """Return a multidigit positive or negative integer consumed from the input"""
        result = ''
        if self.current_char == '-':
            result += self.current_char
            self.advance()
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return Token(INTEGER_CONST, int(result))


    def _id(self):
        """Handle identifiers and reserved keywords"""
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        if(result[0] == 'R' and result[1].isdigit()):
            return Token(REGISTER, result)

        token = RESERVED_COMMANDS.get(result)
        if token == None:
            if self.current_char == ':':
                token = Token(LABEL, result + ':')
                self.advance()
            else:
                token = Token(GOTO_LABEL, result)


        return token

    def get_next_token(self):
        """Lexical analyzer (tokenizer)
            This method is responsible for breaking a sentence
            apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return self._id()

            if self.current_char.isdigit() or self.current_char == '-':
                return self.number()

            if self.current_char == ':' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(ASSIGN, ':=')

            if self.current_char == ':':
                self.advance()
                return Token(COLON, ':')

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '*':
                self.advance()
                return Token(MULTIPLY, '*')

            if self.current_char in ['=', '<', '>']:
                operator = self.current_char
                self.advance()
                return Token(IF_OPERATOR, operator)

        return Token(EOL, None)