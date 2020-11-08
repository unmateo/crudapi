from sqlalchemy.orm import Session


class DeleteService:
    def __init__(self, model):
        self.model = model

    def delete(self, db: Session, model, *args, **kwargs):
        """ """
        db.delete(model)
        db.flush()
        return model
