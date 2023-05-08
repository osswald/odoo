from odoo import models, fields


class KeyPermission(models.Model):
    _name = "key_management.permission"

    name = fields.Char("Label", required=True)
