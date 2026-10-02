# -*- coding: utf-8 -*-
# Copyright 2026, Weboffice IT-Service und Marketing GmbH & Co KG

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    lead_stakeholder_ids = fields.One2many(
        'crm.stakeholder',
        'partner_id',
        string='Stakeholder in Lead/Opportunity',
    )
