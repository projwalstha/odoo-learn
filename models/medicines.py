from odoo import models, fields

class HostipalMedicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'Medicines'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    _rec_name = 'medicine_name'

    medicine_name = fields.Char(string="Name", required='True')
    medicine_usage = fields.Text(string='Description')
    unit_price = fields.Integer(string="Unit Price(RS)")