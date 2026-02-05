from odoo import http
import json
from urllib.parse import parse_qs

class PatientApi(http.Controller):
    @http.route('/p1/patient',methods=['POST'],type='http',auth='none',csrf=False)
    def post_patient(self):
        print("Inside post_patient method")
        try:
         args=http.request.httprequest.data.decode()
         vals=json.loads(args)
         res=http.request.env['clinic.patient'].sudo().create(vals)

         if res:
             return http.request.make_json_response({
                 "message":"Patient added successfully :)"
             },status=200)

        except Exception as error:
            return http.request.make_json_response({
                "message":str(error)
            },status=400)


    @http.route('/p1/patient/<int:patient_id>',methods=['GET'],type='http',auth='none',csrf=False)
    def get_patient(self,patient_id):
        try:
            patient_id=http.request.env['clinic.patient'].search([('id','=',patient_id)])
            if not patient_id:
                return http.request.make_json_response({
                    "message":"ID does not exist"

                },status=400)

            return http.request.make_json_response({
                "name": patient_id.name or "",
                "gender": patient_id.gender or "",
                "age": patient_id.age or "",
                "email": patient_id.email or "",
                "address":patient_id.address or ""
                 })

        except Exception as error:
            return http.request.make_json_response({
                "message":str(error)
            },status=400)

    @http.route('/p/patients', methods=['GET'], type='http', auth='none', csrf=False)
    def get_patients(self):
        try:
            parms=parse_qs(http.request.httprequest.query_string.decode('utf-8'))
            patient_domain=[]
            if parms.get('gender'):
                patient_domain+=[('gender','=',parms.get('gender')[0])]
            patient_ids=http.request.env['clinic.patient'].search(patient_domain)
            if not patient_ids:
                return http.request.make_json_response({
                    "message":"There are not any record"
                },status=400)

            return http.request.make_json_response([{
                "name": patient_id.name or "",
                "gender": patient_id.gender or "",
                "age": patient_id.age or "",
                "email": patient_id.email or "",
                "address": patient_id.address or ""
            }for patient_id in patient_ids],status=200)

        except Exception as error:
            return http.request.make_json_response({
                "message":str(error)
            },status=400)

    @http.route('/p1/patient/<int:patient_id>',methods=['PUT'],type='http',auth='none',csrf=False)
    def update_patient(self,patient_id):
        try:
            patient_id=http.request.env['clinic.patient'].sudo().search([('id','=',patient_id)])
            if not patient_id:
                 return http.request.make_json_response({
                     "message":"Id does not exist"
                 },error=400)
            args=http.request.httprequest.data.decode()
            vals=json.loads(args)
            patient_id.write(vals)
            return http.request.make_json_response({
                "message":"Updated Successfully",
                 "Name": patient_id.name,
            },status=200)
        except Exception as error:
            return http.request.make_json_response({
                "message":str(error)
            },status=400)


    @http.route('/p1/patient/<int:patient_id>',methods=["DELETE"],type='http',auth='none',csrf=False)
    def delete_patient(self,patient_id):
        try:
            patient_id=http.request.env['clinic.patient'].sudo().search([('id','=',patient_id)])
            if not patient_id:
                return http.request.make_json_response({
                    "message":"Id does not exist"
                },status=400)

            patient_id.unlink()
            return http.request.make_json_response({
                "message":"Deleted Successfully!"
            },status=200)

        except Exception as error:
            return http.request.make_json_response({
                "message":str(error)
            },status=400)










