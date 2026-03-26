from odoo import models, fields

class DuAn(models.Model):
    _inherit = 'qldu.du_an'
    
    cong_viec_ids = fields.One2many('qlcv.cong_viec', 'du_an_id', string="Công việc")
