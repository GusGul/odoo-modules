from odoo import fields, models, api, _
from lxml import etree
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

class school_student(models.Model):
    _name = "school.student"
    _sql_constraints = [
        ('positive_fees', 'CHECK (student_fees>=0)', 'Valor da mensalidade não pode ser negativo')
    ]

    name = fields.Char(string="Nome", required=True, copy=False) # copy=False ao duplicar, o nome virá vazio
    school_id = fields.Many2one("school", string="Nome da Escola", required=True) # default={id} tipo: default=1
    hobby_list = fields.Many2many("hobby", "student_hobby_rel", "student_id", "hobby_id",
                                  string="Hobbies", copy=True)
    is_virtual_school = fields.Boolean(related="school_id.is_virtual_class", string="Suporte para Aula Online",
                                       #store=True <- Isso armazena a variável "is_virtual_school" no banco de dados
                                       )
    school_address = fields.Text(related="school_id.address", string="Address")
    currency_id = fields.Many2one("res.currency", string="Moeda", default=6)
    student_fees = fields.Monetary(string="Mensalidade Escolar", default=900.00) # é possível transformar um float em monetary com widgets
    active = fields.Boolean(string="Ativo", default=True, copy=False #, default=True
                            )
    birthDate = fields.Date(string="Data de Nascimento")
    age = fields.Integer(compute="_calcula_idade", string="Idade", store=True)

# INÍCIO - TESTAR OS COMANDOS DO TERMINAL
    compute_function = fields.Integer(compute="_compute_func")

    @api.depends("compute_function")
    def _compute_func(self):
        self.env['school.student'].search([('name','like','%a%')])
        return 0
# FIM - TESTAR OS COMANDOS DO TERMINAL

    @api.depends("birthDate")
    def _calcula_idade(self):
        today = fields.Date.today()
        for student in self:
            if student.birthDate:
                delta = today.year - student.birthDate.year - ((today.month, today.day) < (student.birthDate.month, student.birthDate.day))
                student.age = delta
            else:
                student.age = 0

    def custom_method(self):
        try:
            self.ensure_one() # garante que apenas um RECORD está sendo passado. Caso receba multiple records, dará um erro.
            print(self.name)
            print(self.schoold_id.name)
        except ValueError:
            pass

# INÍCIO DOS MÉTODOS DE OVERWRITE
    # @api.model_create_multi       # multiple values, crete multiple profiles at a time
    @api.model # decorator          # overwrite / single value, crete single profile at a time
    def create(self, values):
        # values['active'] = True   # active default True METODO 1
        rtn = super(school_student, self).create(values)
        # rtn.active = True         # active to True METODO 2
        return rtn

    # sem decorator
    def write(self, values):        # write é o método de "edit", para alterar dados
        rtn = super(school_student, self).write(values)
        if not self.hobby_list:     # tratamento de erro, tornando o campo hobby_list como required
            raise UserError(_("Por favor selecione pelo menos um hobby."))
        return rtn

    def copy(self, default = {}): # overwrite do método duplicate
        default['active'] = False # alunos duplicados/copiados serão criados com "active" False por padrão
        default['name'] = "copy of "+self.name
        rtn = super(school_student, self).copy(default=default)
        return rtn

    def unlink(self):             # overwrite do método delete
        for stud in self:
            if stud.student_fees > 0:
                raise UserError("Você não pode deletar esse %s perfil de estudante"%stud.name)
        rtn = super(school_student, self).unlink()
        return rtn

    @api.model
    def default_get(self, fields_list=[]): # retorna todos os valores de campoes com algo preenchido, como default
        rtn = super(school_student, self).default_get(fields_list)
        # rtn['active'] = True
        # rtn['name'] = "Default Name"
        return rtn

    # from lxml import etree
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False): # retorna a view do form
        res = super(school_student, self).fields_view_get(view_id=view_id, view_type=view_type,
                                                           toolbar=toolbar, submenu=submenu)

        if view_type == "form":
            doc = etree.XML(res['arch'])
            age_field = doc.xpath("//field[@name='age']")
            if age_field:
                # Adicionado uma label na form view
                age_field[0].addnext(etree.Element('label',{'string':'Custom label do fields_view_get'}))

            address_field = doc.xpath("//field[@name='school_address']")
            if address_field:
                address_field[0].set("string", "fields_view_get Endereço")

            res['arch'] = etree.tostring(doc, encoding='unicode')

        if view_type == "tree":
            # Adicionado um field na tree view
            doc = etree.XML(res['arch'])
            school_field = doc.xpath("//field[@name='school_id']")
            if school_field:
                school_field[0].addnext(etree.Element('field',{'string':'Mensalidade fields_view_get', 'name':'student_fees'}))
            res['arch'] = etree.tostring(doc, encoding='unicode')

        return res
    print()
# FIM DOS MÉTODOS DE OVERWRITE

# método browse encontra dados especificos pelo ID
# método search mostra todos os "records" do database, se usado con len mostra a quantidade (com parâmetros é um SELECT)
# search(['|',('','',''),('','','')]) -> where cond_1 ou cond_2
# read retorna um dictionary com os dados do BD
# read_group retornar um dictionary com os dados do BD com um "where" filtrando apenas os pertencentes a um "Group". Por
    # exemplo, agrupar estudantes por escolas, e dar um read apenas dos estudantes da "first school".
    # read_group() / read_group([('','','')]) / read_group([], fields=[''], groupby=[''], limit=, offset=, orderby='')
# get_metadata retorna os metadados da view
# fields_get retorna um dictionary com todos os fields e seus atributos e valores. Field especifico: field.get(['name'])
# fields_view_get()