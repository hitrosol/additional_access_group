
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Add Access Group for more specific use case",
    "version": "14.0.1.0.0",
    "author": "PT Solusi Aglis Indonesia",
    "category": "Generic",
    "license": "AGPL-3",
    "website": "https://solusiaglis.co.id",
    "depends": ["hr_expense", "hr_expense_petty_cash"],
    "data": [
        "security/res_group.xml",
        "security/access_right_expense_assistant.xml",
        "security/access_right_account_assistant.xml",
        "security/ir_rule_account_assistant.xml",
        "security/ir_rule_expense_assistant.xml",
        "views/hr_expense_views.xml",
        "views/account_menuitem.xml",
    ],
    "installable": True,
    "maintainers": ["hitrosol"],
}
