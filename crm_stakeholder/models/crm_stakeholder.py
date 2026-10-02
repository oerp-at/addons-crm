# -*- coding: utf-8 -*-
# Copyright 2026, Weboffice IT-Service und Marketing GmbH & Co KG

from odoo import models, fields


class CrmStakeholder(models.Model):
    _name = 'crm.stakeholder'
    _description = 'CRM Stakeholder'

    role_id = fields.Many2one(
        'project.stakeholder.role',
        string='Stakeholder Role',
        required=True,
        ondelete='restrict',
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Stakeholder',
        required=True,
        index=True,
        ondelete='cascade',
    )
    lead_id = fields.Many2one(
        'crm.lead',
        required=True,
        index=True,
        ondelete='cascade',
    )
    note = fields.Text()
