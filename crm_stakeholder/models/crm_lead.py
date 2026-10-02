# Copyright 2026 Weboffice IT-Service und Marketing GmbH & Co KG
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    stakeholder_ids = fields.One2many(
        'crm.stakeholder',
        'lead_id',
        string='Stakeholders',
    )
