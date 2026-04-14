"""
из текста делает токены
x + 5 -> [x, +, 5]
"""

from minilang.tokens import Token, TokenType, KEYWORDS
from pydantic import BaseModel, PositiveInt


class Lexer(BaseModel):
    def __init__(self, text: str):
        self.text: str = text
        self.pos: int = 0
        self.current_char: str = self.text[self.pos] if len(self.text) > 0 else None

        self.line: PositiveInt = 1
        self.column: PositiveInt = 1

        self.len_text: int = len(self.text)

    def advance(self):

        if self.current_char == "\n":
            self.line += 1
            self.column = 0

        self.column += 1
        self.pos += 1

        if self.pos >= self.len_text:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self) -> Token:
        number: list[str] = []
        has_dot: bool = False
        start_column = self.column

        while self.current_char is not None and (
            self.current_char.isdigit() or self.current_char == "."
        ):

            if self.current_char == ".":
                if has_dot:
                    break
                has_dot = True
            number.append(self.current_char)
            self.advance()

        str_result: str = "".join(number)
        if has_dot:
            result: float = float(str_result)
        else:
            result: int = int(str_result)

        return Token(
            type_=TokenType.NUMBER, value=result, line=self.line, column=self.column
        )

    def get_next_token(self) -> Token:
        """Лексический анализатор: определяет, какой токен идет следующим."""
        pass

    def tokenize(self):
        """Удобная функция, чтобы сразу получить весь список токенов."""
        pass
