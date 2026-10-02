# -*- coding: utf-8 -*-
# Copyright 2026, Weboffice IT-Service und Marketing GmbH & Co KG

from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    stakeholder_ids = fields.One2many(
        'crm.stakeholder',
        'lead_id',
        string='Stakeholders',
    )
