from odoo import fields, models, api

class AuthorProfile(models.Model):
    _name = "author.profile"

    name = fields.Char(string="Nome", required=True, size=45)
    book_list = fields.One2many("library", "author_id", string="Livros")
    count_books = fields.Integer(compute="_compute_count_books", string="Quantidade de Livros")

    @api.depends('book_list')
    def _compute_count_books(self):
        for r in self:
            r.count_books = len(r.book_list)