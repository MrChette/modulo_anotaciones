from odoo import models, fields

class anotaciones(models.Model):
    _name="create.anotaciones"

    note = fields.Char("Nota")
    descripcion = fields.Char("Description")
    date = fields.dateTime("Date")