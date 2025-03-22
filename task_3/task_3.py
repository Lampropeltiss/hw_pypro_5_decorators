from datetime import datetime
from functools import wraps
import pyjokes


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = old_function(*args, **kwargs)
        f_name = old_function.__name__
        args_str = 'args = ' + ', '.join([str(i) for i in args])
        kwargs_str = 'kwargs = ' + ', '.join(f'{key}={val}' for key, val in kwargs.items())

        info = [start, f_name, args_str, kwargs_str, str(result)]
        output = '{:17} | {:12} | {:10} | {:10} | {:10} \n'.format(*info)
        with open('task_3.log', 'w', encoding='utf-8') as file:
            file.write(output)
        return result
    return new_function


@logger
def get_pyjoke(language):
    return pyjokes.get_joke(language)


if __name__ == '__main__':
    get_pyjoke('ru')
