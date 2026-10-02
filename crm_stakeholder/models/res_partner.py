# Copyright 2026 Weboffice IT-Service und Marketing GmbH & Co KG
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    lead_stakeholder_ids = fields.One2many(
        'crm.stakeholder',
        'partner_id',
        string='Stakeholder in Lead/Opportunity',
    )
