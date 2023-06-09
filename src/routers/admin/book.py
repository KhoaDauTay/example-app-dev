from sqladmin import ModelView

from src.database.models import BookModel
from src.helpers.permission import check_role_access, check_role_view


class BookAdmin(ModelView, model=BookModel):
    column_list = [BookModel.id, BookModel.name, BookModel.description, BookModel.price, BookModel.stock, BookModel.list_book_author, BookModel.category, BookModel.store, BookModel.created_at, BookModel.updated_at]

    def is_accessible(self, request) -> bool:
        return check_role_access(request)

    def is_visible(self, request) -> bool:
        return check_role_view(request, self.identity)