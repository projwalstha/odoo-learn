# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string="patient")


class HospitalPatient(models.Model):
    _name = 'hospital.patients'
    _description = 'Hospital Table'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    _rec_name = 'patient_name'
    _order = 'id desc'

    @api.constrains('patient_age')
    def check_age(self):
        if self.patient_age<=0:
            raise ValidationError('The age cannot be neagative')
        elif self.patient_age>=150:
            raise ValidationError('The age is not valid')


    def open_patient_appointment(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    @api.depends('patient_age')
    def set_age_group(self):
            if self.patient_age > 18:
                self.age_group = 'major'
            else:
                self.age_group = 'minor'

    def get_appointment_count(self):
        self.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])

    patient_name = fields.Char(string='Name', required=True, track_visibility="always")
    patient_age = fields.Integer('Age', required=True, track_visibility="always",)
    patient_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], default='male', required='True',track_visibility="always")
    age_group = fields.Selection([
        ('major', 'major'),
        ('minor', 'minor')
    ], compute='set_age_group',store= True)
    notes = fields.Text('Notes',track_visibility="always")
    image = fields.Binary(string='Image',track_visibility="always")
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default= lambda self: _('New'))
    appointment_count = fields.Integer('Appointment', compute='get_appointment_count')
    patient_appointment = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
                vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

    @api.model
    def get_patients_list(self):
        patient = self.search([])
        patient_list = []
        for pat in patient:
            val = {
                'patient_name': pat.patient_name,
                'patient_age': pat.patient_age,
                'patient_gender': pat.patient_gender,
                'notes':pat.notes,
            }
            patient_list.append(val)
        return patient_list
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
