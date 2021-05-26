from odoo import models, fields, api, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'hospital.doctor'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    _rec_name = 'doctor_name'

    doc_id = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True,
                         default=lambda self: _('New'))
    doctor_name = fields.Char(string="Name", required='True')
    doctor_age = fields.Integer(string='Age')
    doctor_speciality = fields.Char(string='Speciality')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True)
    doctor_dob = fields.Date(string='Date of Birth')
    doctor_phone = fields.Char(string='Phone Number')

    @api.model
    def create(self, vals):
        if vals.get('doc_id', _('New')) == _('New'):
            vals['doc_id'] = self.env['ir.sequence'].next_by_code('doctor.sequence') or _('New')
        result = super(HospitalDoctor, self).create(vals)
        return result

    @api.model
    def delete_doctor(self, doc_id):
        print(doc_id)
        self.search([('doc_id', '=', doc_id)]).unlink()

    @api.model
    def get_doctor(self, doc_id):
        data = self.search([('doc_id', '=', doc_id)])
        data_dict = {
            'id':data.id,
            'doctor_name': data.doctor_name,
            'doctor_gender': data.gender,
            'doctor_speciality': data.doctor_speciality,
            'doctor_phone': data.doctor_phone,
            'doctor_age': data.doctor_age,
        }
        return data_dict
