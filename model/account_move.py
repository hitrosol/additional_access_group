# Copyright 2019 Ecosoft Co., Ltd (https://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import _, fields, models
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"
    
    def action_post(self):
        if self.env.user.has_group('additional_access_group.group_account_assistant'):
            self.sudo().action_post()
            return super(AccountMove, self).action_post()


