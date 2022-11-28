from odoo import models, fields, api


class Partner(models.Model):
    _inherit = "res.partner"

    # @api.model
    # def create(self, vals):
    #     print("User Env ", self.env)
    #     print("User Env ", self.env.user)
    #     print("User Env ", self.env.company)
    #     print("User Env ", self.env.companies)
    #     print("User Env ", self.env.context)
    #
    #     print(" partner values ", vals)
    #
    #     if 'company_id' not in vals:
    #         vals['company_id'] = self.env.company.id
    #
    #     gus_company = self.env['res.company'].browse(1)
    #
    #     return super(Partner, self).create(vals)  # método return super normal
    #     # return super(Partner, self.with_context(self.env.context)).create(vals)
    #     # return super(Partner, self.with_user(self.env.user)).create(vals)
    #     # return super(Partner, self.with_company(gus_company)).create(vals)
