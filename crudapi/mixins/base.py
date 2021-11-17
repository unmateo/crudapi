def default_prefix(orm_model):
    return f"/{orm_model.__tablename__}"


def default_title(orm_model):
    return orm_model.__tablename__.capitalize()


def default_tags(orm_model):
    return [default_title(orm_model)]


def router_extras(orm_model, **kwargs):
    kwargs.setdefault("tags", default_tags(orm_model))
    kwargs.setdefault("prefix", default_prefix(orm_model))
    return kwargs
