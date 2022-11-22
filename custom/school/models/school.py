from odoo import fields, models, api

class SchoolProfile(models.Model):
    _name = "school"

    def default_establish_date(self):

        return '2000-01-01'

    def default_open_date(self):

        return '2000-01-01 12:00:00'

    # O "trim" por default é True, use apenas para alternar para false
    name = fields.Char(string="Nome da Escola", help="This is School Name", required=True, trim=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Telefone")
    is_virtual_class = fields.Boolean(string="Suporte para Aula Online")
    result = fields.Float(string="Result", digits=(2, 3))
    address = fields.Text(string="Endereço", required=True)
    establish_date = fields.Date(string="Establish Date", default=lambda lm: lm.default_establish_date())
    open_date = fields.Datetime(string="Open Date", default=lambda lm: lm.default_open_date())
    school_type = fields.Selection([('public','Escola Pública'),
                                    ('private','Escola Particular')],
                                   string="Tipo de Escola") # default=
    documents = fields.Binary(string="Documentos")
    document_name = fields.Char(string="Nome do Arquivo")
    # Sem os "max_" e o "verify_resolution" o Image funcionará como um Binary
    school_image = fields.Image("Imagem", max_width=100, max_height=100, verify_resolution=True)
    school_description = fields.Html(string="Descrição") # default="<b>bold</b>" pode receber tags html
    # school_rank = fields.Integer(string="Rank", required=True, size=6)
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="Auto Rank", store=True)

    @api.depends("school_type") # transforma a atualização do compute imediata
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    @api.model
    def name_create(self, name):        # altera o metodo create name
        # rtn = self.create({'name':name})
        # rtn = self.create({"name":name,"email":"default@mail.com"})
        # return rtn.name_get()[0]
        return super(SchoolProfile, self).name_create(name)