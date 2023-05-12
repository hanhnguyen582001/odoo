from odoo import fields,models
class EducationClass(models.Model):
    _name='education.class'
    _description='Education Class'
    
    name=fields.Char(string='Name',required=True)
    school_id= fields.Many2one('education.school',string='School',required=True)
    teacher_ids = fields.Many2many('res.partner', string='Teachers')