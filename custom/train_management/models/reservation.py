from odoo import models, fields, api


class Reservation(models.Model):
    _name = "train_management.reservation"
    _description = "Reservation"

    name = fields.Char("Label", required=True)
    commission_nr = fields.Char("Commission Nr.")
    phone_number = fields.Char("Phone number")
    email = fields.Char("E-Mail")
    amount = fields.Integer("Amount", required=True)
    type = fields.Selection(
        selection=[
            ("seat", "Seat"),
            ("gastro", "Gastro"),
        ],
        string="Reservation type",
        default="seat",
        copy=False,
        required=True,
    )
    comment = fields.Text("Comment")
    train = fields.Many2one("train_management.train")
    day_planning = fields.Many2one("train_management.day_planning", compute="_compute_day_planning", store=True)

    @api.depends('train')
    def _compute_day_planning(self):
        for reservation in self:
            reservation.day_planning = reservation.train.circuit.day_planning
    