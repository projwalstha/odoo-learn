from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']

    def action_confirm(self):
        self.state = 'pharmacy'

    def action_done(self):
        self.state = 'complete'

    name = fields.Char(string="Appointment", required=True, copy=False, index=True,
                       readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patients', string="Patient", required=True, )
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    notes = fields.Text('Registration Note')
    doctor = fields.Many2one('hospital.doctor')
    doctor_note = fields.Text('Note')
    pharmacy_note = fields.Text('Note')
    prescription = fields.One2many('prescription.medicine', 'appointment_id', string="Prescriptions")
    buy_medicine = fields.One2many('hospital.pharmacy', 'appoint_id', string="Buy Medicine")
    appointment_date = fields.Date(string="Appointment Date", required=True)
    state = fields.Selection(selection=[
        ('doctor', 'Doctor'),
        ('pharmacy', 'Pharmacy'),
        ('complete', 'Complete'),
        ('cancel', 'Cancel')
    ], string='Status', readonly=True, copy=False, default='doctor')
    # pharmacy_bill = fields.One2many('pharmacy.bill', 'app_id')
    vat = fields.Integer('VAT%', )
    discount = fields.Integer('Discount%', )
    g_total = fields.Integer('Total', compute='get_gtotal', )

    @api.onchange('buy_medicine.price')
    def get_gtotal(self):
        untaxed_total = 0
        print(self._origin.id)
        pharm_objs = self.env['hospital.pharmacy'].search([('appoint_id', '=', self._origin.id)])
        print(self.buy_medicine)
        print(pharm_objs)
        for rec in pharm_objs:
            untaxed_total += rec.price
        taxed_amt = 0.01 * self.vat * untaxed_total + untaxed_total
        discounted = taxed_amt - 0.01 * self.discount * taxed_amt
        self.g_total = discounted

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result


class PrescriptionMedicine(models.Model):
    _name = 'prescription.medicine'
    _description = 'Prescribed Medicine'
    _rec_name = 'medicine_id'

    medicine_id = fields.Many2one('hospital.medicine', string='Medicines', required=True)
    doctor_note = fields.Text(name='Note')
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment ID")


class HospitalPharmacy(models.Model):
    _name = 'hospital.pharmacy'
    _description = 'Pharmacy'

    appoint_id = fields.Many2one('hospital.appointment', string="Appointment ID")
    prescribed = fields.Many2one('prescription.medicine', string='Prescribed medicine', )
    quantity = fields.Integer('Quantity')
    unit_price = fields.Integer('Unit_price', related='prescribed.medicine_id.unit_price')
    price = fields.Integer('Price', compute='get_subtotal')

    @api.onchange('appoint_id')
    def compute_prescribed(self):
        print(self.env.context.get('default_id'))
        act_id = self.env.context.get('default_id')
        print(act_id)
        return {'domain': {'prescribed': [('appointment_id', '=', act_id)]}}

    @api.depends('quantity')
    def get_subtotal(self):
        for rec in self:
            # unit_price = self.prescribed.medicine_id.unit_price
            # print(unit_price)
            rec.price = rec.unit_price * rec.quantity

# class PharmacyBill(models.Model):
#     _name = 'pharmacy.bill'
#     _description = 'Pharmacy Bill'
#
#     pharmacy_id = fields.Many2one('hospital.pharmacy')
#     g_total = fields.Integer('Grand Total', compute='get_gtotal')
#     discount = fields.Integer('Discount')
#     vat = fields.Integer('VAT')
#     app_id = fields.Many2one('hospital.appointment')
#
#     @api.depends('discount', 'vat')
#     def get_gtotal(self):
#         untaxed_total = 0
#         app = self.env.context.get('default_id')
#         pharm_objs = self.env['hospital.pharmacy'].search([('id', '=', app)])
#         for rec in pharm_objs:
#             untaxed_total += rec.price
#         taxed_amt = 0.01 * self.tax * untaxed_total + untaxed_total
#         discounted = taxed_amt - 0.01 * self.discount * taxed_amt
#         self.g_total = discounted
