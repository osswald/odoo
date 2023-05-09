from odoo import models, fields


class Circuit(models.Model):
    _name = "train_management.circuit"
    _description = "Circuit"

    name = fields.Char("Label", required=True)
    distance = fields.Integer("distance")
    frequency = fields.Integer("Frequency")
    day_planning = fields.Many2one("train_management.day_planning", required=True, readonly=True)
    vehicles = fields.Many2many("train_management.vehicle")
    train_ids = fields.One2many("train_management.train", "circuit")
