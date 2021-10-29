from samples.apps.library import Library
from samples.data import populate_db


app = Library()

populate_db()
