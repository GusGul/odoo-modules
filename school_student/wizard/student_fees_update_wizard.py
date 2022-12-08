from odoo import api, models, fields


class StudentFeesUpdateWizard(models.TransientModel):
    _name = "student.fees.update.wizard"

    total_fees = fields.Float(string="Mensalidade")

    def update_student_fees(self):
        print("Isso é um método do wizard")

        self.env['school.student'].browse(self._context.get("active_ids")).update({'total_fees':self.total_fees})
        return True

class StudentFeesUpdateWizard(models.TransientModel):
    _inherit = "student.fees.update.wizard"

    parent_name = fields.Char(string="Parent Name")

    def update_student_fees(self):
        print("Isso é um método herdado")

        # Sem Super statement
        # return True

        # Com Super statement
        variable = super(StudentFeesUpdateWizard, self).update_student_fees()
        return variable