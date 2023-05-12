from odoo import fields, models

class EducationSchool(models.Model):
    _name='education.school'
    _description='School'
    
    name= fields.Char(string='Name', translate=True,required=True)
    code=fields.Char(string='Code',copy=False)
    class_ids = fields.One2many('education.class', 'school_id', string='Classes')
    student_ids= fields.One2many('education.student','school_id',string='Students')
    
    def get_all_students(self):
        student=self.env['education.student']
        all_students=student.search([])
        print('All students: ',all_students)
        
    def create_schools(self):
    # Giá trị để tạo bản ghi student 01
        student_01 = {
            'name': 'Student 01',
        }
        # Giá trị để tạo bản ghi student 02
        student_02 = {
            'name': 'Student 02'
        }
        # Giá trị để tạo bản ghi lớp học
        school_value = {
            'name': 'School 01',
            # Đồng thời tạo mới 2 học sinh
            'student_ids': [
                (0, 0, student_01),
                (0, 0, student_02)
            ]
        }
        record = self.env['education.school'].create(school_value)