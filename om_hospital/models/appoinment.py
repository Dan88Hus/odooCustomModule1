from odoo import api, fields, models


class HospitalAppoinment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital appointment"
    # comodel_name = "hospital.patient" ta diyebilirdik or first argument dont need comodel label
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    _rec_name = 'patient_id'
    # fields.Date.context_today will return the current date
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    # to get fireld from another table, we use related field, and need to create field in this table as well
    # gender field getirmek icin (patient.py dan), Many2one oldugundan . operator kullanabiliyoruz
    # related fields by default are readonly, we can use readonly=False, edit ettigimiz related ana tabloda save etmis olur
    gender = fields.Selection(string='Gender', related='patient_id.gender')
    # ref values will come from patient.py table
    ref = fields.Char(string='Reference')
    # prescription for html field
    prescription = fields.Html(string='Prescription')
    # for priority(star) field we use selection field
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very High')], string="Priority", help="Gives star for priority")
    state = fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In Consultation'),
        ('done','Done'),
        ('cancel','Cancelled')], string="Status", default='draft', required=True)
    # state is reserved keyword in odoo to define status of document


    # to define onchange of field , keyword is onchange_fieldName
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
        # print("self", self)

    def action_test(self):
        print("clicked")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'click Successfull!',
                'type': 'rainbow_man'
            }
        }
