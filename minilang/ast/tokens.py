from enum import StrEnum
from typing import Any
from pydantic import BaseModel, PositiveInt


class TokenType(StrEnum):
    NUMBER = "NUMBER"
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"

    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"

    ASSIGN = "ASSIGN"
    EQ = "EQ"

    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    COMMA = "COMMA"
    SEMI = "SEMI"

    LET = "LET"
    PRINT = "PRINT"
    IF = "IF"
    ELSE = "ELSE"

    EOF = "EOF"
    ILLEGAL = "ILLEGAL"


KEYWORDS = {
    "let": TokenType.LET,
    "print": TokenType.PRINT,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
}


class Token(BaseModel):
    type_: TokenType
    value: Any
    line: PositiveInt = 1
    column: PositiveInt = 1

    def __repr__(self):
        if self.value:
            return f"Token({self.type_.name}, '{self.value}')"
        return f"Token({self.type_.name})"
