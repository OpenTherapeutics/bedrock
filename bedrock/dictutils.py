from collections import Mapping
from copy import deepcopy
 
def deep_update(d, u):
    '''
    TODO
    '''
    for k, v in u.items():
        if isinstance(v, Mapping):
            r = deep_update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d


def overlay(base, partial=None):
    '''
    TODO
    '''
    if not partial:
        return base

    return deep_update(deepcopy(base), partial)
