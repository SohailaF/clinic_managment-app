from odoo import models,fields

class DoctorsAppointment(models.Model):
    _name='doctors.appointment'
    _description = 'Doctors appointment model'


    doctor_id=fields.Many2one('clinic.doctors',string="Doctor")
    appointment=fields.Datetime()
