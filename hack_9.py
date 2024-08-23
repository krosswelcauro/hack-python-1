"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    resultado = len(result)
    while resultado < 4:
        result.insert(1, '@')
        resultado = len(result)
        if resultado < 5:
            result.insert(3, '@')
            resultado = len(result)
        if resultado < 6:
            result.insert(5, '@')
        return result  