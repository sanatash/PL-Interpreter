from src.spl_token import *

class SPlParser():
    """
    Parser - finds the  structure in the stream of lexical tokens
    """
    # register_dict = {"R0": None, "R1": None, "R2": None, "R3": None, "R4": None,
    #                  "R5": None, "R6": None, "R7": None, "R8": None, "R9": None}

    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()
        self.current_command = self.__update_command()

    def __str__(self):
        return f"Lexer object: {self.lexer}, current_token object: {self.current_token}"

    def __repr__(self):
        return self.__str__()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def get_current_token(self):
        return self.current_token

    def __update_command(self):
        """
             Checks if current token is the command or label, stores in parser what is current command name
             or "LABEL" token if it's label type
             :return: current command name or "LABEL"
             :rtype: string
        """
        if self.current_token.value in RESERVED_COMMANDS.keys():
            return self.current_token.value
        elif self.current_token.type == LABEL:
            return "LABEL"

    def get_command(self):
        """
        Returns current command as stored in parser object
        :return: current command name or "LABEL"
        :rtype: string
        """
        return self.current_command

    def parse(self):
        """
        Parser - does parsing of single command line of the program
        :return:
        :rtype:
        """
        return

    def evaluate(self):
        return None
