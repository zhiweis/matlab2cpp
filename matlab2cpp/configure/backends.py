
Project = "program"
Program = "program"
Includes = "program"
Funcs = "program"
Inlines = "program"
Structs = "program"
Struct = "program"
Headers = "program"
Log = "program"
Header = "program"
Main = "func_return"
Error = "program"
Warning = "program"
Counter = "structs"
Inline = "program"
Include = "program"
Block = "code_block"
For = "code_block"
While = "code_block"
Switch = "code_block"
Case = "code_block"
Otherwise = "code_block"
Branch = "code_block"
If = "code_block"
Elif = "code_block"
Else = "code_block"
Tryblock = "code_block"
Try = "code_block"
Catch = "code_block"
Statement = "code_block"
Assigns = "code_block"
Expr = "expression"
Exp = "expression"
Elexp = "expression"
Mul = "expression"
Minus = "expression"
Elmul = "expression"
Matrixdivision = "expression"
Elementdivistion = "expression"
Leftmatrixdivision = "expression"
Leftelementdivision = "expression"
Plus = "expression"
Colon = "expression"
Gt = "expression"
Ge = "expression"
Lt = "expression"
Le = "expression"
Ne = "expression"
Eq = "expression"
Band = "expression"
Bor = "expression"
Land = "expression"
Lor = "expression"
Paren = "expression"
Neg = "expression"
Not = "expression"
Ctranspose = "expression"
Transpose = "expression"
All = "expression"
End = "expression"
Break = "expression"
Return = "expression"
Matrix = "matrix"
Cell = "cell"
Int = "int"
Float = "double"
Imag = "cx_double"
String = "string"
Lambda = "func_lambda"
Lcomment = "code_block"
Bcomment = "code_block"
Ecomment = "code_block"
Fvar = "struct"
Cvar = "cell"
Cget = "cell"
Fget = "structs"
Sget = "structs"
Nget = "struct"
Cset = "cell"
Fset = "structs"
Sset = "structs"
Nset = "struct"
Resize = "cube_common"
Verbatim = "verbatim"

def Var(node):
    if node.type != "TYPE":
        node.backend = node.type
def Get(node):
    if node.type != "TYPE":
        node.backend = node.type

def Vector(node):
    node.backend = "matrix"

    # matrix surround struct converts it to array
    if node and node[0].backend == "struct":
        declare = node.func[0][node.func[0].names.index(node[0].name)]
        if declare.backend == "structs":
            node.backend = "structs"

def Func(node):
    returns = node[1]
    if node.name[:1] == "_":
        node.backend = "func_lambda"
    elif len(returns) == 1:
        node.backend = "func_return"
    else:
        node.backend = "func_returns"
def Returns(node):
    if node.parent.name[:1] == "_":
        node.backend = "func_lambda"
    elif len(node) == 1 or node.parent.cls == "Main":
        node.backend = "func_return"
    else:
        node.backend = "func_returns"
def Params(node):
    returns = node.parent[1]
    if node.parent.name[:1] == "_":
        node.backend = "func_lambda"
    elif len(returns) == 1 or node.parent.cls == "Main":
        node.backend = "func_return"
    else:
        node.backend = "func_returns"
def Declares(node):
    returns = node.parent[1]
    if node.parent.name[:1] == "_":
        node.backend = "func_lambda"
    elif len(returns) == 1 or node.parent.cls == "Main":
        node.backend = "func_return"
    else:
        node.backend = "func_returns"


def Assign(node):
    if node[1].type == "func_lambda":
        node.backend = "func_lambda"
