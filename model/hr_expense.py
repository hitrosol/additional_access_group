from odoo import api, fields, models

class HrExpenseInherit(models.Model):
    _inherit = "hr.expense"
    
    @api.model
    def _get_employee_id_domain(self):
        res = super(HrExpenseInherit,self)._get_employee_id_domain()
        if self.user_has_groups('additional_access_group.group_hr_expense_assistant'):
            res = "['|', ('company_id', '=', False), ('company_id', '=', company_id)]"  # Then, domain accepts everything
        return res


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    def action_sheet_move_create(self):
        if self.env.user.has_group('additional_access_group.group_account_assistant'):
            return super(HrExpenseSheet, self.sudo()).action_sheet_move_create()
        return super(HrExpenseSheet, self).action_sheet_move_create()

