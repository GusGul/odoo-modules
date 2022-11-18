from odoo import fields, models, api #, _
# from odoo.exceptions import UserError

class SchoolProfile(models.Model):
    _name = "school"
    _inherit = _name

    school_list = fields.One2many("school.student", "school_id", string="Estudantes",
                                  #limit=5
                                  )

# overwrite do método de required do Odoo, para obrigar a preencher a lista com pelo menos 1 aluno na criação
    # @api.model
    # def create(self, values):
    #     rtn = super(SchoolProfile, self).create(values)
    #     if not rtn.school_list:
    #         raise UserError(_("A lista de estudantes está vazia"))
    #     return rtn