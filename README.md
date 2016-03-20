# project_serial_numbers
======================
Track serial numbers for Projects, and their components.
This module uses two classes:
- Components
- Groups


Components
---------
Each lowest level component has:

- Name
- Category
- Model/Type
- Serial Number
- Firmware Version
- Notes
- Component Group (it can belong to one Component Group)

A collection of lowest-level components can be grouped into a Component Group.
The Component Group can contain more grouped items


Component Groups
---------------

- Name
- Project
- Partner (Customer)
- Serial Number
- Notes
- Parent Component Group (it can belong to one Component Group)
- Sub-Groups (it may contain multiple sub groups)
- Components (it may contain muliple components)

Duplicate names can be used and are uniquely identified by differnent project paths. There's an intuitive nomencalture used so the full path/tree to any node is explicity stated like so:

EXAMPLES
--------
Group View:
-----------
 - Project 1 > Top Group
 - Project 1 > Top Group > First Branch
 - Project 1 > Top Group > First Branch > Second Branch
 - Project 1 > Main Group 2
 - Project 1 > Main Group 2 > MG2 Branch 1


Component View:
---------------
 - Project 1 > Top Group > First Branch > Second Branch > Component 1
 - Project 1 > Top Group > First Branch > Second Branch > Component 2
 - Project 1 > Main Group 2 > Component MG1
 - Project 1 > Main Group 2 > MG2 Branch 1 > Component  MG2
