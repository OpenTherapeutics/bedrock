from collections import Mapping
from copy import deepcopy

def _deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, Mapping):
            r = _deep_update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d
 

def overlay(base, partial=None):
    '''
    Condisering `base` as a declarative pseudo-schema dict, iterate over `partial`
    hierarchically augmenting a deepcopy of `base`. 

    Different from `collections.Chainmap` and various other `MergeDict` packages
    in that changes are effected in placejanf not via a wrapper for stack-based
    implementions such as Django's `Context`.

    '''
    base = deepcopy(base)
    if not partial:
        return base

    if not isinstance(partial, Mapping):
        raise TypeError('`partial` must be a Mapping type')
        
    return _deep_update(base, partial)


