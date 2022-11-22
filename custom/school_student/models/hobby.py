from odoo import fields, models


class Hobbies(models.Model):
    _name = "hobby"

    name = fields.Char("Hobby")
