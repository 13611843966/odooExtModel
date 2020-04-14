# -*- coding: utf-8 -*-

import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sms_update_pwd = fields.Boolean(string=u'修改密码', config_parameter='sms_base.default_sms_update_pwd')
    sms_phone_login = fields.Boolean(string=u'手机号登陆', config_parameter='sms_base.default_sms_phone_login')

