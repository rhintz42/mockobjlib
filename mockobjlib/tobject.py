

class TObject(object):
    def __init__(self, *args, **kwargs):
        for key in kwargs:
            # This is like doing self[key] = kwargs[key], but allows you to
            #   do it on the class object
            setattr(self, key, kwargs[key])

    def t_method(self):
        return 'cool'
    
