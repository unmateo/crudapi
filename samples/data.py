from crudapi.core.database import get_session
from crudapi.core.logging import logger
from crudapi.services.create import CreateService
from samples.models import Author
from samples.models import AuthorCreate
from samples.models import Book
from samples.models import BookCreate


authors = {
    "Franco Armani",
    "Javier Pinola",
    "Jonatan Maidana",
    "Milton Casco",
    "Gonzalo Montiel",
    "Leonardo Ponzio",
    "Enzo Pérez",
    "Exequiel Palacios",
    "Ignacio Fernandez",
    "Gonzalo Martinez",
    "Lucas Pratto",
}

books = {
    "Winter is comming",
    "The Kingsroad",
    "Lord Snow",
    "Cripples, Bastards, and Broken Things",
    "The Wolf and the Lion",
    "A Golden Crown",
    "You Win or You Die",
    "The Pointy End",
    "Baelor",
    "Fire and Blood",
    "The North Remembers",
}


def populate_db():
    with get_session() as session:
        authors_service = CreateService(Author)
        books_service = CreateService(Book)
        for author, book in zip(authors, books):
            a = authors_service.create(session, AuthorCreate(name=author))
            logger.info(f"Created {a}")
            b = books_service.create(session, BookCreate(title=book, author_id=a.id))
            logger.info(f"Created {b}")
