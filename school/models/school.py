from odoo import fields, models, api


class SchoolProfile(models.Model):
    _name = "school"
    _sql_constraints = [
        ('name_unique', 'unique (name)', "Erro: Esse nome já existe")
    ]

    # _order = "name, id desc" # altera o order by até mesmo na ORM e no método search, permanentemente.
    # _rec_name = "email" # isso altera o campo que aparece nas relações de outras views de "name" para o campo "email".

    # _log_access = False # os campos do odoo como create_date, create_uid, write_date, write_uid não serão criados -
    # - automaticamente, se o log access for false desde a criação da tabela, essas colunas não serão nem criadas

    def default_establish_date(self):

        return '2000-01-01'

    def default_open_date(self):

        return '2000-01-01 12:00:00'

    # O "trim" por default é True, use apenas para alternar para false
    school_seq_name = fields.Char("School Code")
    name = fields.Char(string="Nome da Escola", help="This is School Name", required=True, trim=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Telefone")
    is_virtual_class = fields.Boolean(string="Suporte para Aula Online")
    result = fields.Float(string="Result", digits=(2, 3))
    address = fields.Text(string="Endereço")
    establish_date = fields.Date(string="Establish Date", default=lambda lm: lm.default_establish_date())
    open_date = fields.Datetime(string="Open Date", default=lambda lm: lm.default_open_date())
    school_type = fields.Selection([('public', 'Escola Pública'),
                                    ('private', 'Escola Particular')],
                                   string="Tipo de Escola")  # default=
    documents = fields.Binary(string="Documentos", groups="school.access_school_mid_level_group")
    document_name = fields.Char(string="Nome do Arquivo")
    # Sem os "max_" e o "verify_resolution" o Image funcionará como um Binary
    school_image = fields.Image("Imagem", max_width=100, max_height=100, verify_resolution=True)
    school_description = fields.Html(string="Descrição")  # default="<b>bold</b>" pode receber tags html
    # school_rank = fields.Integer(string="Rank", required=True, size=6)
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="Auto Rank", store=True)
    school_number = fields.Integer(string="Código da Escola")
    currency_id = fields.Many2one("res.currency", string="Moeda", default=6)
    active = fields.Boolean(default=True)

    @api.model
    def create(self, vals):
        vals['school_seq_name'] = self.env['ir.sequence'].next_by_code("school")
        return super(SchoolProfile, self).create(vals)

    @api.depends("school_type")  # transforma a atualização do compute imediata
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    @api.model
    def name_create(self, name):  # altera o metodo create name
        # rtn = self.create({'name':name})
        # rtn = self.create({"name":name,"email":"default@mail.com"})
        # return rtn.name_get()[0]
        return super(SchoolProfile, self).name_create(name)

    # com name_get, pode-se alterar um many2one tipo adicionando o tipo de escola após o nome da escola no selection
    # se o método custom name_get for encontrado, o _rec_name usará ele ao invés do default "'name' field".
    def name_get(self):
        student_list = []
        for school in self:
            name = school.name
            if school.school_type:
                name += " ({})".format(school.school_type)
            student_list.append((school.id, name))
        return student_list

    # SPECIAL COMMANDS: Criação, edição, deleção, etc...
    # criar/create
    def specialCommand0(self):
        # Primeira forma de criar um 'child model' por meio de um 'parent model' existente.
        # std_obj = self.env['school.student']
        # std_id = std_obj.create({'name': 'Student ONE', 'school_id': self.id, 'birthDate': '2000-01-01'})

        # Criando parent model e child model.
        # std_obj = self.env['school.student']
        # school_id = self.create({'name':'Kapil Sharma Show'})
        # std_obj.create({'name': 'Kapil Student ONE', 'school_id': school_id.id, 'birthDate': '2000-01-02'})
        # std_obj.create({'name': 'Kapil Student TWO', 'school_id': school_id.id, 'birthDate': '2000-01-03'})
        # std_obj.create({'name': 'Kapil Student THREE', 'school_id': school_id.id, 'birthDate': '2000-01-04'})
        # std_obj.create({'name': 'Kapil Student FOUR', 'school_id': school_id.id, 'birthDate': '2000-01-05'})
        # std_obj.create({'name': 'Kapil Student FIVE', 'school_id': school_id.id, 'birthDate': '2000-01-06'})

        # Criando parent model e child model usando special command.
        # self.create(
        #     {'name': 'Babita School', 'school_list': [(0, 0, {'name': 'Babita Student 1', 'birthDate': '2000-01-01'}),
        #                                               (0, 0, {'name': 'Babita Student 2', 'birthDate': '2000-01-02'})]})

        # self.write({'school_list': [(0, 0, {'name': 'Babita Student 3', 'birthDate': '2000-03-01'})]})
        pass

    # alterar/update
    def specialCommand1(self):
        # Alterando o child model por meio do parent model, não precisa usar esse método
        # for stud in self.school_list:
        #     stud.name = stud.name + " Special Command"
        #     stud.total_fees = 3600
        #     stud.student_fees = 12000

        # Alterando o child model por meio do parent model com um 'special command'
        # vals = {'school_list': []}
        # for stud in self.school_list:
        #     vals['school_list'].append([1, stud.id, {'name':stud.name+".",
        #                                              'total_fees':1000,
        #                                              'student_fees':4500}])
        #
        # self.write(vals)

        # método ruim com update, não precisa usar assim
        # for stud in self.school_list:
        #     stud.update({'name': stud.name+".",
        #                  'total_fees':stud.total_fees+1})
        # método bom com write, pode-se usar isso ao invés de special command
        # for stud in self.school_list:
        #     stud.write({'name': stud.name + ".",
        #                 'total_fees': stud.total_fees + 1})
        pass

    # deletar/delete
    def specialCommand2(self):
        # deleta sem usar o unlink, usando o special command, deleta PERMANENTEMENTE
        self.write({'school_list': [(2, 21, 0)]})  # deleta o estudante PERMANENTEMENTE

    # dessassociar/unlink
    def specialCommand3(self):
        # "deleta" usando o special command, desassocia o estudante da escola atual
        self.write({'school_list':[(3, 20, 0)]}) # faz unlink da escola nesse estudante

    # associar/link
    def specialCommand4(self):
        self.write({'school_list':[(4, 20, 0)]}) # associa o estudante de id 20 à esta escola

    # clear()
    def specialCommand5(self):
        # Limpa/desassocia todos os estudantes da lista desta escola
        # self.write({'school_list':[(5, 0, 0)]})
        pass
    # set - specialCommand6 está em school_student / comando many2many