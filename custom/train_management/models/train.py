from odoo import models, fields


class Train(models.Model):
    _name = "train_management.train"
    _description = "Train"

    name = fields.Char("Label", required=True)
    description = fields.Text("description")
    frequency = fields.Integer("Frequency")
    start_station = fields.Many2one("train_management.station")
    end_station = fields.Many2one("train_management.station")
