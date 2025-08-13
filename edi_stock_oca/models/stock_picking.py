# Copyright 2022 OCA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = ["stock.picking", "edi.exchange.consumer.mixin"]

    # Override all methods to trigger EDI exchange after picking state changes.
    # ``stock.picking.state`` is computed so we cannot rely
    # on the write as done by the consumer mixin.`
    def action_confirm(self):
        self._action_edi_trigger_before()
        result = super().action_confirm()
        self._action_edi_trigger_after()
        return result

    def _action_done(self):
        self._action_edi_trigger_before()
        result = super()._action_done()
        self._action_edi_trigger_after()
        return result

    def action_cancel(self):
        self._action_edi_trigger_before()
        result = super().action_cancel()
        self._action_edi_trigger()
        return result

    def _action_edi_trigger_after(self):
        for picking in self:
            picking._event("on_edi_stock_picking_state_change").notify(
                picking, state=picking.state
            )

    def _action_edi_trigger_before(self):
        for picking in self:
            picking._event("on_edi_stock_picking_before_state_change").notify(
                picking, state=picking.state
            )
