
import abc

class SPlParser(metaclass=abc.ABCMeta):

    """
    Parser - finds the  structure in the stream of lexical tokens
    """
    # register_dict = {"R0": None, "R1": None, "R2": None, "R3": None, "R4": None,
    #                  "R5": None, "R6": None, "R7": None, "R8": None, "R9": None}

    def __init__(self, lexer):
        self.lexer = lexer

    def __str__(self):
        return f"Lexer object: {self.lexer}, current_token object: {self.lexer.get_current_token()}"

    def __repr__(self):
        return self.__str__()

  
    @abc.abstractmethod
    def parse(self):
        """
        Parser - does parsing of single command line of the program
        :return:
        :rtype:
        """
        return

    @abc.abstractmethod
    def evaluate(self):
        return None
