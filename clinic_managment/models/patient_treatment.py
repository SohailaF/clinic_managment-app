from odoo import models,fields,api
from odoo.api import onchange
from odoo.exceptions import ValidationError
from odoo.tools.populate import compute


class PatientTreatment(models.Model):
    _name='patient.treatment'
    _description="Patient treatment model"

    treatment_name=fields.Selection([
       ('general checkup','General Checkup' ),
       ('follow up','Follow Up'),
       ('consultation','Consultation'),
       ('x-ray','X-Ray'),
       ('lab test','Lab Test'),
       ('ecg','ECG'),
       ('ultrasound','Ultrasound'),
       ('medication','Medication'),
       ('injection','Injection'),
       ('observation','Observation'),
       ('emergency treatment','Emergency Treatment')

    ])
    notes=fields.Text()
    treatment_type=fields.Selection([
         ('consultation','Consultation'),
         ('session','Session'),
         ('procedure','Procedure'),
         ('minor surgery','Minor Surgery')

    ],compute='_compute_treatment_type',store=True)
    patient_ids=fields.Many2many('clinic.patient',string='Patient')
    price=fields.Float()
    paid=fields.Float()
    remain=fields.Float(compute='_compute_remain')

    @api.constrains('price')
    def _check_price(self):
        for rec in self:
            if rec.price<=0:
                print("Price must be grater than zero!")
                raise ValidationError("Price can not be less than zero!")
    @api.constrains('paid')
    def _check_paid(self):
        for rec in self:
            if rec.paid<=0:
                print("The value must be grater than zero!")
                raise ValidationError("The value must be grater than zero!")
    @api.depends('price','paid')
    def _compute_remain(self):
        for rec in self:
            rec.remain=rec.price-rec.paid

    @api.depends('treatment_name')
    def _compute_treatment_type(self):
        for rec in self:
            if (rec.treatment_name in ['general checkup','follow up','consultation']):
                rec.treatment_type= 'consultation'
            elif rec.treatment_name in['x-ray','lab test','ecg','ultrasound']:
                rec.treatment_type = 'procedure'
            elif rec.treatment_name in ['medication','injection','observation'] :
                rec.treatment_type = 'session'
            elif (rec.treatment_name=='emergency treatment'):
                rec.treatment_type = 'minor surgery'

    @api.constrains('treatment_name','treatment_type')
    def _check_treatment_type(self):
        for rec in self:
            if rec.treatment_name in ['general checkup','follow up','consultation'] and rec.treatment_type!= 'consultation':
                raise ValidationError("Treatment type must be 'Consultation' for this treatment!")
            elif rec.treatment_name in ['x-ray', 'lab test', 'ecg', 'ultrasound'] and rec.treatment_type != 'procedure':
                raise ValidationError("Treatment type must be 'Procedure' for this treatment!")
            elif rec.treatment_name in ['medication', 'injection', 'observation'] and rec.treatment_type != 'session':
                raise ValidationError("Treatment type must be 'Session' for this treatment!")
            elif rec.treatment_name == 'emergency treatment' and rec.treatment_type !='minor surgery':
                raise ValidationError("Treatment type must be 'Minor Surgery' for Emergency Treatment!")



