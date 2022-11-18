from odoo import fields, models


class LibraryProfile(models.Model):
    _name = "library"

    name = fields.Char(string="Nome", required=True, size=45)
    author_id = fields.Many2one("author.profile", string="Autor", required=True)
    category_ids = fields.Many2many("category", "book_category_rel", "library_id", "category_id",
                                string="Categorias")
    # category = fields.Selection([('1', 'Drama'), ('2', 'Conto'), ('3', 'Crônica'), ('4', 'Poesia'),
    #                              ('5', 'Ação'), ('6', 'Aventura'), ('7', 'Terror'), ('8', 'Suspense'),
    #                              ('9', 'Distópico'), ('10', 'Futurista'), ('11', 'Fantasia'), ('12', 'Guia')],
    #                             string="Categoria")
    pages = fields.Integer(string="Nº de Páginas", required=True)
    publisher = fields.Char(string="Editora", required=True, size=45, default="Odoo")
    release_date = fields.Date(string="Data de Lançamento")
    description = fields.Text(string="Descrição")
