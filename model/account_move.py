# Copyright 2019 Ecosoft Co., Ltd (https://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_post(self):
        if self.env.user.has_group('additional_access_group.group_account_assistant'):
            return super(AccountMove, self.sudo()).action_post()
        return super(AccountMove, self).action_post()


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    def action_create_payments(self):
        if self.env.user.has_group('additional_access_group.group_account_assistant'):
            return super(AccountPaymentRegister, self.sudo()).action_create_payments()
        return super(AccountPaymentRegister, self).action_create_payments()



class AccountPayment(models.Model):
    _inherit = "account.payment"

    def action_post(self):
        if self.env.user.has_group('additional_access_group.group_account_assistant'):
            return super(AccountPayment, self.sudo()).action_post()
        return super(AccountPayment, self).action_post()





