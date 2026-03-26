from odoo import models, fields, api

class CongViec(models.Model):
    _name = 'qlcv.cong_viec'
    _description = 'Quản lý công việc'

    name = fields.Char("Tên công việc", required=True)
    mo_ta = fields.Text("Mô tả công việc")
    trang_thai = fields.Selection([
        ('can_lam', 'Cần làm'),
        ('dang_lam', 'Đang làm'),
        ('hoan_thanh', 'Hoàn thành'),
    ], string="Trạng thái", default='can_lam')
    han_chot = fields.Date("Hạn chót")
    
    du_an_id = fields.Many2one('qldu.du_an', string="Dự án")
    nguoi_thuc_hien_id = fields.Many2one('nhan_vien', string="Người thực hiện")
