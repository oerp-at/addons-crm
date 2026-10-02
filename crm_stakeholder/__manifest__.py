# Copyright 2026 Weboffice IT-Service und Marketing GmbH & Co KG
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "CRM Stakeholder",
    "version": "19.0.1.0.1",
    "category": "Customer Relationship Management",
    "website": "https://github.com/OCA/crm",
    "author": "Weboffice IT-Service und Marketing GmbH & Co KG,"
    "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "summary": "Manage stakeholders of leads/opportunities and their roles",
    "depends": [
        "crm",
        "project_stakeholder",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/crm_lead_views.xml",
        "views/stakeholder_menu_views.xml",
        "views/res_partner_views.xml",
    ],
}
