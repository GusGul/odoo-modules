from odoo import fields, models

class AuthorProfile(models.Model):
    _name = "author.profile"

    name = fields.Char(string="Nome", required=True, size=45)
    book_list = fields.One2many("library", "author_id", string="Livros")