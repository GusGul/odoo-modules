from odoo import fields, models, api, _, registry
from lxml import etree
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


# class student_test(models.Model): # teste para adicionar um CUSTOM NAME para a tabela criada do model
#     _name = "student.test" # cria uma tabela no banco de dados chamada "student_test"
#     _table = "student_test_testing" # ao invés da tabela usar o _name, a tabela criada se chamará "student_test_testing"
#
#     name = fields.Char()
# class Address(models.Model):
#     _name = "address"
#     _rec_name = "street"
#
#     street = fields.Char(string="Rua")
#     street_one = fields.Char(string="Bairro")
#     city = fields.Char(string="Cidade")
#     state = fields.Char(string="Estado")
#     country = fields.Char(string="País")
#     zip_code = fields.Char(string="CEP")

class school_student(models.Model):
    _name = "school.student"
    # _inherit = "address"
    _sql_constraints = [
        ('positive_fees', 'check (student_fees > 0)', "Erro: Valor da mensalidade não pode ser negativo"),
        ('maiority', 'check (age > 17)', "Erro: Você precisa ser maior de 18 anos"),
        ('unique_name', 'unique (name)', 'Erro: Por favor informe outro nome, nome dado já existe.')
    ]
    # _sequence = "custom_seq_name"

    name = fields.Char(string="Nome", required=True, copy=False)  # copy=False ao duplicar, o nome virá vazio
    roll_number = fields.Char(string="Roll Number")
    school_id = fields.Many2one("school", string="Nome da Escola", required=True,
                                # Multiple Domains
                                # domain="[('school_type','=','public'),
                                # ('is_virtual_class','=',True)]"
                                domain="[('currency_id','=',currency_id)]")  # default={id} tipo: default=1
    # apenas escolas com a mesma unidade monetária do estudante irão aparecer nas opções, por causa do domain
    hobby_list = fields.Many2many("hobby", "student_hobby_rel", "student_id", "hobby_id",
                                  string="Hobbies")
    is_virtual_school = fields.Boolean(related="school_id.is_virtual_class", string="Suporte para Aula Online",
                                       # store=True <- Isso armazena a variável "is_virtual_school" no banco de dados
                                       )
    school_address = fields.Text(related="school_id.address", string="Address")
    currency_id = fields.Many2one("res.currency", string="Moeda", default=6)
    student_fees = fields.Monetary(string="Mensalidade",
                                   default=900.00)  # é possível transformar um float em monetary com widgets
    total_fees = fields.Float(string="Mensalidade 2")
    active = fields.Boolean(string="Ativo", default=True, copy=False)
    birthDate = fields.Date(string="Data de Nascimento")
    age = fields.Integer(compute="_calcula_idade", string="Idade", store=True)

    def specialCommand6(self): #many2many
        ids = [15, 19, 9, 12]
        self.write({"hobby_list":[(6, 0, ids)]})

    # @api.onchange("school_id") # no perfil estudante, apenas a unidade monetária da escola selecionada aparecerá nas opções de currency
    # def _onchange_school(self):
    #     currency_id = 0
    #     if self.school_id:
    #         currency_id = self.school_id.currency_id.id
    #     return {"domain": {'currency_id':[('id','=',currency_id)]}}

    @api.model
    def _change_roll_number(self):
        # Este método é usada para adicionar um roll number ao estudante
        for stud in self.search([('roll_number', '=', False)]):
            print(stud.roll_number)
            stud.roll_number = 'STD' + str(stud.id)

    # def wiz_open(self):
    #
    #     return self.env['ir.actions.act_window']._for_xml_id("school_student.student_fees_update_action")
    #
    #     return {'type': 'ir.actions.act_window',
    #             'res_model': 'student.fees.update.wizard',
    #             'view_mode': 'form',
    #             'target': 'new'}

    @api.depends("birthDate")
    def _calcula_idade(self):
        today = fields.Date.today()
        for student in self:
            if student.birthDate:
                delta = today.year - student.birthDate.year - (
                        (today.month, today.day) < (student.birthDate.month, student.birthDate.day))
                student.age = delta
            else:
                student.age = 0

    def custom_method(self):
        try:
            self.ensure_one()  # garante que apenas um RECORD está sendo passado. Caso receba multiple records, dará um erro.
            print(self.name)
        except ValueError:
            pass

    # INÍCIO DOS MÉTODOS DE OVERWRITE
    # @api.model_create_multi       # multiple values, crete multiple profiles at a time
    @api.model  # decorator          # overwrite / single value, crete single profile at a time
    def create(self, values):
        # values['active'] = True   # active default True METODO 1
        rtn = super(school_student, self).create(values)
        # rtn.active = True         # active to True METODO 2
        return rtn

    # sem decorator
    # def write(self, values):  # write é o método de "edit", para alterar dados
    #     rtn = super(school_student, self).write(values)
    #     if not self.hobby_list:  # tratamento de erro, tornando o campo hobby_list como required
    #         raise UserError(_("Por favor selecione pelo menos um hobby."))
    #     return rtn

    def copy(self, default={}):  # overwrite do método duplicate
        default['active'] = False  # alunos duplicados/copiados serão criados com "active" False por padrão
        default['name'] = "copy of " + self.name
        rtn = super(school_student, self).copy(default=default)
        return rtn

    # esse método ovewrite não permite o estudante ser apagado caso a mensalidade seja maior que 0
    # def unlink(self):  # overwrite do método delete
    #     for stud in self:
    #         if stud.student_fees > 0:
    #             raise UserError("Você não pode deletar esse %s perfil de estudante" % stud.name)
    #     rtn = super(school_student, self).unlink()
    #     return rtn

    @api.model
    def default_get(self, fields_list=[]):  # retorna todos os valores de campoes com algo preenchido, como default
        rtn = super(school_student, self).default_get(fields_list)
        # rtn['active'] = True
        # rtn['name'] = "Default Name"
        return rtn

    # from lxml import etree
    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):  # retorna a view do form
    #     res = super(school_student, self).fields_view_get(view_id=view_id, view_type=view_type,
    #                                                       toolbar=toolbar, submenu=submenu)
    #
    #     if view_type == "form":
    #         doc = etree.XML(res['arch'])
    #         age_field = doc.xpath("//field[@name='age']")
    #         if age_field:
    #             # Adicionado uma label na form view
    #             age_field[0].addnext(etree.Element('label', {'string': 'Custom label do fields_view_get'}))
    #
    #         address_field = doc.xpath("//field[@name='school_address']")
    #         if address_field:
    #             address_field[0].set("string", "fields_view_get Endereço")
    #
    #         res['arch'] = etree.tostring(doc, encoding='unicode')
    #
    #     if view_type == "tree":
    #         # Adicionado um field na tree view
    #         doc = etree.XML(res['arch'])
    #         school_field = doc.xpath("//field[@name='school_id']")
    #         if school_field:
    #             school_field[0].addnext(etree.Element('field', {'string': 'Mensalidade fields_view_get',
    #                                                             'name': 'student_fees'}))
    #         res['arch'] = etree.tostring(doc, encoding='unicode')
    #
    #     return res

    def custom_button_method(self):

        # self.env.cr.execute("insert into school_student(name, active) values('from button click', True)")
        # self.env.cr.commit()

        # self._cr.execute("insert into school_student(name, active) values('from button click', True)")
        # self._cr.commit()

        print("Env............ ", self.env)
        print("User id........ ", self.env.uid)
        print("Current user... ", self.env.user)
        print("Super user..... ", self.env.su)
        print("Language....... ", self.env.lang)
        print("Cr............. ", self.env.cr)
        print("\nVocê clicou em mim, senhor(a) ", self.name)
        self.custom_method()

        # change cursor
        # new_cr = registry(self.env.cr.dbname).cursor()
        # partner_id = self.env['res.partner'].with_env(self.env(cr=new_cr)).create({"name": " New Env CR Partner."})
        # partner_id.env.cr.commit()

    print()
# FIM DOS MÉTODOS DE OVERWRITE

# método browse encontra dados especificos pelo ID

# método search mostra todos os "records" do database, se usado con len mostra a quantidade (com parâmetros é um SELECT)
# search(['|',('','',''),('','','')]) -> where cond_1 ou cond_2
# método _search: diferente do search, retornar uma LISTA/ARRAY, enquanto o search retornava um RECORD SET.

# read retorna um dictionary com os dados do BD

# read_group retornar um dictionary com os dados do BD com um "where" filtrando apenas os pertencentes a um "Group". Por
# exemplo, agrupar estudantes por escolas, e dar um read apenas dos estudantes da "first school".
# read_group() / read_group([('','','')]) / read_group([], fields=[''], groupby=[''], limit=, offset=, orderby='')

# get_metadata retorna os metadados da view

# fields_get retorna um dictionary com todos os fields e seus atributos e valores. Field especifico: field.get(['name'])

# fields_view_get()

# stud_obj = self.env['school.student'] || stud_list = stud_obj.search([]) || stud_list.filtered(lambda lm: lm.student_fees >= 1000)

# método mapped(odoo)(igual "map"), stud_list.mapped(lambda lm: lm.school_id) mostra todos os school_ids presentes, sem
# repetição, dentro dos alunos. stud_list.mapped(lambda lm: lm.currency_id) mostra apenas "6", o unico currency usado (BRL)

# método sort() - stud_list.sorted(key='school_id') ou key='id', etc. || stud_list.sorted(lambda lm: lm.id) igual key='id'.
# "reverse=True" funciona como um "order by desc", por padrão o reverse é False assim como order by asc.

# env.user retonar res.users(1,) que é o usuário odoo atual que está logado, utilizando o odoo.
# usando env da para ter acesso a todos os CRUDS
# dir(env) retorna diversos parametros para usar no env.

# with_context() -
