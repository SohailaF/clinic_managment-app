from odoo import models,fields

class ClinicDoctors(models.Model):
    _name="clinic.doctors"
    _description = "Clinic doctors model"

    name = fields.Char(required=True)
    age = fields.Integer()
    phone = fields.Char(required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ])
    doctor_specialty=fields.Char(required=True,string="Specialty")
    salary=fields.Float(required=True)
    email=fields.Char()
    appointment_ids=fields.One2many('doctors.appointment','doctor_id',string='Appointment')
