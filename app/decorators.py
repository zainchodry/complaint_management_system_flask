from flask import abort
from flask_login import current_user

def role_required(role):
    def wrapper(fn):
        def decorated(*args, **kwargs):
            if current_user.role != role:
                abort(403)
            return fn(*args, **kwargs)
        decorated.__name__ = fn.__name__
        return decorated
    return wrapper
