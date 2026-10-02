# -*- coding: utf-8 -*-
# Copyright 2026, Weboffice IT-Service und Marketing GmbH & Co KG

# noinspection PyStatementEffect
# pylint: disable=missing-readme
{
    'name': 'CRM Stakeholder',
    'version': '19.0.1.0.1',
    'category': 'CRM',
    'website': 'https://weboffice.at',
    'author': 'Weboffice IT-Service und Marketing GmbH & Co KG',
    'license': 'OPL-1',
    'summary': 'Manage crm stakeholders and their roles',
    'depends': [
        'crm',
        'project_stakeholder',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/stakeholder_menu_views.xml',
        'views/res_partner_views.xml',
    ],
}
