def flatten(objin):
    if isinstance(objin, dict):
        dout = {}
        for key in objin:
            sub = flatten(objin[key])
            if isinstance(sub, dict):
                for sub_key in sub:
                    dout[".".join((key, sub_key))] = sub[sub_key]
            else:
                dout[key] = sub
        return dout

    elif isinstance(objin, list):
        dout = {}
        for idx in range(len(objin)):
            dout[str(idx)] = flatten(objin[idx])
        return dout
    else:
        return objin

    raise BaseException("Unhandled type")
 

def test():
    d = {'1': 'a', '2': 'b', '3': 'c'}
    d2 = flatten(d)
    print(d2)
    assert d == d2

    d = {
        'a': '1',
        'b': {
            'a': '2',
            'b': '3',
            'c': {
                'a': '4',
                'b': '5',
            },
        },
    }
    d2 = flatten(d)
    print(d2)
    assert d2 == {'a': '1', 'b.a': '2', 'b.b': '3', 'b.c.a': '4', 'b.c.b': '5'}

    d = {
        'a': ['1','2','3'], 
        'b': {
            'c': ['4', '5', '6'],
            'd': '7',
        },
        'e': '8',
    }
    d2 = flatten(d)
    print(d2)
    assert d2 == {'a.0': '1', 'a.1': '2', 'a.2': '3', 'b.c.0': '4', 'b.c.1': '5', 'b.c.2': '6', 'b.d': '7', 'e': '8'}
