from odoo import fields, models, api


class LibraryProfile(models.Model):
    _name = "library"
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'Titulo do livro deve ser unico.'),
        ('positive_page', 'CHECK (pages>0)', 'Numero de paginas deve ser positivo')
    ]

    name = fields.Char(string="Nome", required=True, size=45)
    author_id = fields.Many2one("author.profile", string="Autor", required=True)
    currency_id = fields.Many2one("res.currency", string="Moeda", default=6)
    price = fields.Monetary(string="Preço")
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
    stock = fields.Selection([('stock', 'Em estoque'),
                              ('sold', 'Esgotado')],
                             string="Estoque")
    age_days = fields.Integer(compute='_compute_age', string="Anos de Idade")

    @api.depends('release_date')
    def _compute_age(self):
        today = fields.Date.today()
        for book in self:
            if book.release_date:
                delta = today - book.release_date
                book.age_days = delta.days
            else:
                book.age_days = 0
