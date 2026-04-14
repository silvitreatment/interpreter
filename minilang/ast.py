from typing import List, Any
from interpreter.minilang.tokens import Token
from pydantic import BaseModel


class AstNode(BaseModel):
    pass


class NumberNode(AstNode):
    value: float


class IdentifierNode(AstNode):
    value: str


class BinOpNode(AstNode):
    left: AstNode
    op: Token
    right: AstNode


class VarDeclNode(AstNode):
    name: str
    value: AstNode


class PrintNode(AstNode):
    expression: AstNode


class ProrammNode(AstNode):
    statements: List[AstNode]
