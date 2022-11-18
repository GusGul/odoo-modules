from odoo import fields, models

class Categories(models.Model):
    _name = "category"

    name = fields.Char(string="Categoria")