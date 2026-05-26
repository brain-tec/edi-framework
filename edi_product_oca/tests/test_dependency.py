# Copyright 2026 ForgeFlow S.L. (http://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestDependency(TransactionCase):
    def test_endpoint_module_loaded(self):
        self.assertIn("edi_endpoint_id", self.env["edi.exchange.record"]._fields)
