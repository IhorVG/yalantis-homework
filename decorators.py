#!venv/bin/python

import time
import functools

def timer(function):
    '''Decorator @timer calculate the time of working f.

    '''
    import time
    @functools.wraps(function)

    def _timer(*args, **kw):
        t = time.perf_counter()
        rez = function(*args, **kw)
        t = time.perf_counter() - t
        print('{0} time elapsed {1:.8f}'.format(function.__name__, t))
        return rez
    return _timer

def update_dict(N: int = 2):
    '''Decorator @update_dict multiply value of dict on N.

      '''

    def _update_dict(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if isinstance(result,dict):
                for key, value in result.items():
                    if isinstance(value,str):
                        new_value=value*N
                        result[key]=new_value
            return result
        return wrapper
    return _update_dict

if __name__ == '__main__':
    @timer
    @update_dict(3)
    def f():
        d={'a':'1','q':2}
        n=len(d)
        return d

    print(f())