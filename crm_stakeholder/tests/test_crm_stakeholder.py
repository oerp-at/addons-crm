# Copyright 2026 Weboffice IT-Service und Marketing GmbH & Co KG
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.base.tests.common import BaseCommon


class TestCrmStakeholders(BaseCommon):
    # Since 20.0, BaseCommon runs as a basic internal user
    _test_user_groups = ("sales_team.group_sale_manager",)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Bill Ionaire",
                "email": "bill.ionaire@example.com",
            }
        )
        cls.stakeholder_role = cls.env["project.stakeholder.role"].create(
            {
                "name": "Investor",
            }
        )
        cls.lead = cls.env["crm.lead"].create(
            {
                "name": "Lead",
            }
        )
        cls.crm_stakeholder = cls.env["crm.stakeholder"].create(
            {
                "role_id": cls.stakeholder_role.id,
                "partner_id": cls.partner.id,
                "lead_id": cls.lead.id,
                "note": "Main lead investor",
            }
        )

    def test_lead_has_stakeholders(self):
        self.assertIn(self.crm_stakeholder, self.lead.stakeholder_ids)

    def test_partner_is_stakeholder(self):
        self.assertIn(self.crm_stakeholder, self.partner.lead_stakeholder_ids)
