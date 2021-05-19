from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'hospital.doctor'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string="Name", required='True')
    doctor_age = fields.Integer(string='Age')
    doctor_speciality = fields.Char(string='Speciality')
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')
    ], required=True)
    doctor_dob = fields.Date(string='Date of Birth')
    doctor_phone = fields.Char(string='Phone Number')