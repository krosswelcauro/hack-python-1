"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result.rstrip(result[-1]) + result[7].upper()

    return result