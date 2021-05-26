# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Hospital(http.Controller):
    @http.route('/hospital/patient/', auth='public', website=True)
    def index(self, **kw):
        print("sdjkansdskandkjsandkjsndk")
        print(kw)
        if bool(kw):
            request.env['hospital.patients'].create(kw)
        objs = request.env['hospital.patients'].search([])
        print(objs)
        return request.render('hospital.patients-records', {'objs': objs})

    @http.route('/hospital/PatientForm', auth='public', website=True)
    def PatientForm(self, **kwargs):
        return request.render('hospital.patient-create', {})

    @http.route('/hospital/doctors', auth='public', website=True)
    def DcotorList(self, **kwargs):
        return request.render('hospital.show-doctors')

    # @http.route('/hospital/patient/create', auth='public',website=True)
    # def PatientCreate(self,**kw):
    #     print('==================================')
    #     print(kw)
    #     return "Created"

#     @http.route('/hospital/hospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital.listing', {
#             'root': '/hospital/hospital',
#             'objects': http.request.env['hospital.hospital'].search([]),
#         })

#     @http.route('/hospital/hospital/objects/<model("hospital.hospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital.object', {
#             'object': obj
#         })
