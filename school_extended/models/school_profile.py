from odoo import fields, models


class school_student(models.Model):
    _inherit = "school.student"

    student_full_name = fields.Char(string="Nome Completo")