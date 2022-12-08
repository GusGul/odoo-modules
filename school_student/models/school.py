from odoo import fields, models, api  # , _


# from odoo.exceptions import UserError

class SchoolProfile(models.Model):
    _inherit = "school"

    school_list = fields.One2many("school.student", "school_id", string="Estudantes",
                                  # limit=5
                                  )

    @api.model
    def name_search(self, name, args=None, operator='ilike',
                    limit=100):  # permite na busca por nome do campo do one2many
        args = args or []  # buscar por outros fields além do nome (ex: email)
        if name:
            records = self.search(['|', '|', '|', ('name', operator, name), ('email', operator, name),
                                   ('school_number', operator, name), ('school_type', operator, name)])
            return records.name_get()
        # return self.search([('name', operator, name)]+args, limit=limit).name_get()
        return super(SchoolProfile, self).name_search(name=name, args=args, operator=operator, limit=limit)

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|','|','|',('name', operator, name), ('email', operator, name),
    #                  ('school_number', operator, name), ('school_type', operator, name)]
    #     school_ids = self.search(domain+args, limit=limit)
    #     return school_ids.name_get()

# overwrite do método de required do Odoo, para obrigar a preencher a lista com pelo menos 1 aluno na criação
# @api.model
# def create(self, values):
#     rtn = super(SchoolProfile, self).create(values)
#     if not rtn.school_list:
#         raise UserError(_("A lista de estudantes está vazia"))
#     return rtn
