from odoo import models, fields, api, _, tools


class StudentSchoolDynamicView(models.Model):
    _name = "student.school.dynamic.view"
    _description = "Student and School dynamic view from postgres."
    _auto = False

    school_name = fields.Char(string="Nome da Escola")
    school_phone = fields.Char(string="Telefone da Escola")
    school_email = fields.Char(string="Email da Escola")
    school_type = fields.Selection([('public', 'Escola Pública'),
                                    ('private', 'Escola Particular')],
                                   string="Tipo de Escola")
    student_name = fields.Char(string="Nome do Aluno")
    student_rno = fields.Char(string="RA do Aluno")
    student_fees = fields.Float(string="Mensalidade do Aluno")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
        CREATE OR REPLACE VIEW {} as (
            SELECT std.id as id, 
            std.roll_number as student_rno, std.name as student_name, std.student_fees as student_fees,
            sc.name as school_name, sc.email as school_email, sc.phone as school_phone, sc.school_type as school_type
            FROM school_student as std JOIN school as sc ON std.school_id = sc.id)
        """.format(self._table))