def set_in_class(klass):
    def retval(func):
        setattr(klass, func.__name__, func)
        return func
    return retval

def smooth_step(t):
    return t * t * (3 - 2 * t)

_WHICH_OFFSET = dict(
    top='y_offset',
    bottom='y_offset',
    left='x_offset',
    right='x_offset'
)

_WHICH_SIGN = dict(top=1, bottom=-1, left=-1, right=1)

def _effective_side(sprite, direction):
    return (getattr(sprite, direction) -
            _WHICH_SIGN[direction] *
           getattr(sprite, _WHICH_OFFSET[direction], 0))

def _extreme_side(sprite1, sprite2, direction):
    sign = -_WHICH_SIGN[direction]
    return sign * max(sign * _effective_side(sprite1, direction),
                      sign * _effective_side(sprite2, direction))
    
def collide(sprite1, sprite2):
    return (_extreme_side(sprite1, sprite2, 'bottom') <
            _extreme_side(sprite1, sprite2, 'top')
            and
            _extreme_side(sprite1, sprite2, 'left') <
            _extreme_side(sprite1, sprite2, 'right'))
