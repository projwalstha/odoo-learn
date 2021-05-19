from odoo import models, fields, api


class PharmacyBillReport(models.AbstractModel):
    _name = 'report.hospital.pharmacy_report'
    _description = 'Pharmacy Bill Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('yes')
        print(docids[0])
        doc = self.env['hospital.appointment'].browse(docids[0])
        purchase = self.env['hospital.pharmacy'].search([('appoint_id', '=', docids[0])])
        print(doc)
        print(purchase[1].prescribed[0].medicine_id[0].medicine_name)
        print(purchase)
        medicine_list = []
        for item in purchase:
            print(item.prescribed.medicine_id.medicine_name)
            print(item.prescribed.medicine_id.unit_price)
            print(item.quantity)
            print(item.price)
            vals = {
                'med_name': item.prescribed.medicine_id.medicine_name,
                'unit_price': item.prescribed.medicine_id.unit_price,
                'quantity': item.quantity,
                'price': item.price
            }
            medicine_list.append(vals)
        print(medicine_list)
        print(doc)

        return {
            'doc_model': 'hospital.appointment',
            'data': data,
            'docs': doc,
            'medicine_list': medicine_list

        }
