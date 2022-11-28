from odoo import fields, models


class Hobbies(models.Model):
    _name = "hobby"
    _order = "name"

    name = fields.Char("Hobby")

# TESTE
class Car(models.Model):
    _name = "car"

    name = fields.Char(string="Nome do Carro")
    price = fields.Float(string="Valor")
    car_engine_id = fields.One2many("car.engine", "car_engine_id", string="Motor")

class CarEngine(models.Model):
    _name = "car.engine"
    _inherits = {"car":"car_id"}

    name = fields.Char(string="Nome do Motor do Carro")
    car_id = fields.Many2one("car", string="Carro")
    school_id = fields.Many2one("school", string="Escola", required=True)