# -*- coding: utf-8 -*-
##############################################################################
#
#    Michael Watchorn
#    Copyright (C) 2016-today (www.thewatchorngroup.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models, api

class component_group(models.Model):
    """ A collection of components (or other component groups) used to categorize the components."""
    _name = "project.component_group"
    _order= "project_id,parent_group_id,name"
    name = fields.Char(string="Group Name", compute='_path_name', store=True)
    local_name = fields.Char(string="Group Name")
    project_id = fields.Many2one('project.project', string='Project')
    component_ids = fields.One2many('project.component','group_id', string='Components')
    parent_group_id = fields.Many2one('project.component_group', string='Parent Component Group')
    sub_group_ids = fields.One2many('project.component_group','parent_group_id', string='Sub-Groups', store=True)
    serial_number = fields.Char(string='Serial Number')
    notes = fields.Text(string='Notes', help='''Historical facts about this component group.
     * Was it used for something else before?
     * Was it scavanged from another product?
     * Was it originally meant for another project (if so which)?
     * Was it damaged and/or repaired?
     * Did it show weird behavior?''')
    partner_id = fields.Many2one(related='project_id.partner_id', string='Customer', store=True)

    @api.one
    @api.depends('parent_group_id', 'local_name', 'project_id')
    def _path_name(self):
        parent_name=''
        if self.parent_group_id:
            parent_name = str(self.parent_group_id.name) + ' > '
        if (not self.parent_group_id) and self.project_id:
            parent_name = self.project_id.name + ' > '
        self.name= parent_name + str(self.local_name)




class component(models.Model):
    """ A list of specifications about a component belonging to the project, most importantly it's Serial Number.
    """
    _name = "project.component"
    _order = "category,group_id,name"
    name = fields.Char(string='Name')
    group_id = fields.Many2one('project.component_group', string='Parent Group')
    model_type = fields.Char(string='Model/Type', required=True) #  this SHOULD be a product,product. But I'll need to fill in a much of product parts first.
    serial_number = fields.Char(string='Serial Number')
    firmware_number = fields.Char(string='Firmware Number')
    notes = fields.Text(string='Notes', help='''Historical facts about this component.
     * Was it used for something else before?
     * Was it scavanged from another product?
     * Was it originally meant for another project (if so which)?
     * Was it damaged and/or repaired?
     * Did it show weird behavior?''')
    category = fields.Selection([
                                 ('card', 'PLC Rack Card'),
                                 ('camera', 'Camera'),
                                 ('servo','Servo'),
                                 ('other','Other')
                                 ], required=True, string="Category")

    status = fields.Selection([
                                 ('good', 'Good'),
                                 ('damaged', 'Damaged'),
                                 ('unknown','Unknown')
                                 ], required=True, string="Status")
    partner_id = fields.Many2one(related='group_id.partner_id', string='Customer', store=True)
    path_name = fields.Char(string='Path Name', compute='_path_name', store=True)

    @api.one
    @api.depends('group_id')
    def _path_name(self):
        #pudb.set_trace()
        group_name=''
        if self.group_id:
            group_name = str(self.group_id.name) + ' > '
        return group_name + str(self.name)
