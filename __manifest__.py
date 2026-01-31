{
    'name':"Clinic Managment",
    'version':"1.0",
    'depends':['base'],
    'author':"Sohaila Fetiany",
     'category': 'Services',
     'data':[

         'security/ir.model.access.csv',
         'data/sequence.xml',
         'views/patient_view.xml',
         'views/doctor_view.xml',
         'views/doctors_appointment.xml',
         'views/treatment_view.xml',
         'views/clinic_base_menu.xml',
         'wizard/patient_treatment_wizard.xml',
         'reports/patient_report.xml',


     ],
     'license':"LGPL-3",
     'installable':"True",
     'application':True,

}