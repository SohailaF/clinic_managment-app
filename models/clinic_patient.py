from email.policy import default

from odoo import models,fields,api

class ClinicPatient(models.Model):
    _name='clinic.patient'
    _description = 'Patient model'

    name=fields.Char(required=True)
    age=fields.Integer()
    phone=fields.Char()
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female')
    ])
    email=fields.Char()
    address=fields.Char()
    treatment_ids=fields.Many2many('patient.treatment',string='Treatments')
    visit_ids=fields.One2many('patient.visit','patient_id')
    ref=fields.Char(default='New',readonly=True)

    @api.model
    def create(self, vals):
        res=super().create(vals)
        if res.ref=='New':
            res.ref=self.env['ir.sequence'].next_by_code('Patient_seq')
        return res



    def open_treatment_wizard(self):
        self.ensure_one()
        action=self.env.ref(
            'clinic_managment.patient_treatment_action_wizard'
        ).read()[0]

        action['context']={
            'default_patient_id':self.id
        }
        return action




class PatientVisit(models.Model):
    _name='patient.visit'
    _description = 'Patient Visit'

    visit_date=fields.Datetime()
    reason=fields.Char()
    fees=fields.Float()
    patient_id=fields.Many2one('clinic.patient')

