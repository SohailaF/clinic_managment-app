from odoo import models,fields,api
from odoo.exceptions import ValidationError

class PatientTreatmentWizard(models.TransientModel):
    _name='patient.treatment.wizard'
    _description = 'Patient Treatment wizard'

    treatment_name = fields.Selection([
        ('general checkup', 'General Checkup'),
        ('follow up', 'Follow Up'),
        ('consultation', 'Consultation'),
        ('x-ray', 'X-Ray'),
        ('lab test', 'Lab Test'),
        ('ecg', 'ECG'),
        ('ultrasound', 'Ultrasound'),
        ('medication', 'Medication'),
        ('injection', 'Injection'),
        ('observation', 'Observation'),
        ('emergency treatment', 'Emergency Treatment')

    ])
    notes = fields.Text()
    treatment_type = fields.Selection([
        ('consultation', 'Consultation'),
        ('session', 'Session'),
        ('procedure', 'Procedure'),
        ('minor surgery', 'Minor Surgery')

    ],compute='_compute_treatment_type',store=True, )
    price=fields.Float()

    paid = fields.Float()
    patient_id=fields.Many2one('clinic.patient',string='Patient')
    treatment_id=fields.Many2one('patient.treatment')
    confirm=fields.Boolean(string='Confirm')

    @api.depends('treatment_name')
    def _compute_treatment_type(self):
        for rec in self:
            if (rec.treatment_name in ['general checkup', 'follow up', 'consultation']):
                rec.treatment_type = 'consultation'
            elif rec.treatment_name in ['x-ray', 'lab test', 'ecg', 'ultrasound']:
                rec.treatment_type = 'procedure'
            elif rec.treatment_name in ['medication', 'injection', 'observation']:
                rec.treatment_type = 'session'
            elif (rec.treatment_name == 'emergency treatment'):
                rec.treatment_type = 'minor surgery'

    def create_treatment_record(self):

            self.env['patient.treatment'].create({
                'patient_id':self.patient_id.id,
                'treatment_name':self.treatment_name,
                'treatment_type':self.treatment_type,
                'notes':self.notes,
                'price':self.price,
                'paid':self.paid,


            })

    def action_confirm(self):
        if  self.treatment_name:
            self.create_treatment_record()







