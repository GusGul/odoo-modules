from odoo import fields, models


class SchoolClass(models.Model):
    _name = "school.class"
    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Erro: Já existe uma aula com este nome, tente outro.')
    ]

    name = fields.Char(string="Nome da Aula")
    student_ids = fields.Many2many("school.student", string="Alunos Matriculados")

    def customGet(self):
        pass

class SchoolStudent(models.Model):
    _inherit = "school.student"

    classes_ids = fields.Many2many("school.class", string="Aulas")
