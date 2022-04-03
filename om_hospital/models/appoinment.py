from odoo import api, fields, models

class HospitalAppoinment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital appointment"
    #comodel_name = "hospital.patient" ta diyebilirdik or first argument dont need comodel label
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now )
    #fields.Date.context_today will return the current date
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    # to get fireld from another table, we use related field, and need to create field in this table as well
    # gender field getirmek icin (patient.py dan), Many2one oldugundan . operator kullanabiliyoruz
    #related fields by default are readonly, we can use readonly=False, edit ettigimiz related ana tabloda save etmis olur
    gender = fields.Selection(string='Gender', related='patient_id.gender')



