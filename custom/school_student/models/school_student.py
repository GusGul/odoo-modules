from odoo import fields, models, api, _
from odoo.exceptions import UserError

class school_student(models.Model):
    _name = "school.student"

    name = fields.Char(string="Nome", required=True, copy=False)
    school_id = fields.Many2one("school", string="Nome da Escola", required=True) # default={id} tipo: default=1
    hobby_list = fields.Many2many("hobby", "student_hobby_rel", "student_id", "hobby_id",
                                  string="Hobbies", copy=False)
    is_virtual_school = fields.Boolean(related="school_id.is_virtual_class", string="Suporte para Aula Online",
                                       #store=True <- Isso armazena a variável "is_virtual_school" no banco de dados
                                       )
    school_address = fields.Text(related="school_id.address", string="Address")
    currency_id = fields.Many2one("res.currency", string="Moeda")
    student_fees = fields.Monetary(string="Mensalidade Escolar", default=900.00) # é possível transformar um float em monetary com widgets

    def write(self, values):
        rtn = super(school_student, self).write(values)
        if not self.hobby_list:
            raise UserError(_("Por favor selecione pelo menos um hobby."))
        return rtn