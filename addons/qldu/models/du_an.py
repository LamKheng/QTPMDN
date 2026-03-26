from odoo import models, fields, api

class DuAn(models.Model):
    _name = 'qldu.du_an'
    _description = 'Quản lý dự án'

    name = fields.Char("Tên dự án", required=True)
    mo_ta = fields.Text("Mô tả dự án")
    ngay_bat_dau = fields.Date("Ngày bắt đầu")
    ngay_ket_thuc = fields.Date("Ngày kết thúc")
    
    quan_ly_id = fields.Many2one('nhan_vien', string="Quản lý dự án")
