"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    res = result.upper()
    lista = []
    for letra in res:
        lista.append(letra)
    lista[1:3] = ["0", "0"]
    lista[4] = "1"
    lista[6] = "@"
    return lista