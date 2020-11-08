from pydantic import create_model


def update(base):
    """ Receives a pydantic class and returns a subclass of it with all fields as optional. """
    name = f"{base.__name__}Update"
    model = create_model(name, __base__=base)
    for value in model.__fields__.values():
        value.required = False
    return model
