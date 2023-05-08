from odoo import models, fields


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
    