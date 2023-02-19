from odoo import models, fields

class CreateNotes(models.Model):
    _name="create.notes"
    note = fields.Char("Nota")
    descripcion = fields.Char("Description")
    date = fields.Date("Date")