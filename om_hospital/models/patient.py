from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient description"

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference')
    # normal age field
    # age = fields.Integer(string='Age', tracking=True)
    # computed age field, compute='METHODname'
    age = fields.Integer(string='Age', tracking=True, compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    #     archive/unarchieve model de oluyor, active is special keyword in odo to un/archive
    active = fields.Boolean(string="Active", default=True)
    # for computed field
    date_of_birth = fields.Date(string="Date of Birth")

    # kaydet butonuna nastigimizda tetikleniyor, onchange olabilmesi veya realtime DB olmasi icin @api.depends decorator kullaniyoruz
    @api.depends('date_of_birth')
    def _compute_age(self):
        # we need package to import
        today = date.today()
        # print('today: ', today)
        if self.date_of_birth:
            self.age = today.year - self.date_of_birth.year
        else:
            self.age = 0

