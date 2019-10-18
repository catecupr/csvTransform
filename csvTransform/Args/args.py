import argparse

class Args:

    def __init__(self):

        program_description = '''Changes a csv asset table obtained from the oracle database to match the 
                            inventaries database assets table.'''

        parser = argparse.ArgumentParser(description=program_description)

        ''' --Flags that the user can use in the command line interface (terminal)-- '''

        # Flags for altering values in the oracle csv 
        parser.add_argument('--f_name', action='store', required=True, help='Name of the csv file to be modified.')
        parser.add_argument('--owner', action='store', help='Set all the values in the owner column to the given value.')
        parser.add_argument('--room', action='store', help='Set all the values in the room column to the given value.')
        parser.add_argument('--asset_desc', action='store', help='Set all the values in the asset description column to the given value.')
        parser.add_argument('--serial_num', action='store', help='Set all the values in the serial number column to the given value.')
        parser.add_argument('--po_num', action='store', help='Set all the values in the PO number column to the given value.')
        
        # Flags for altering the values of the missing columns (default is an empty string)
        parser.add_argument('--contact_phone', action='store', default='',help='Set all the values in the contact phone column to the given value.')
        parser.add_argument('--contact_ext', action='store', default='', help='Set all the values in the contact extension column to the given value.')
        parser.add_argument('--department', action='store', default='', help='Set all the values in the department column to the given value.')
        parser.add_argument('--warranty_num', action='store', default='', help='Set all the values in the warranty column to the given value.')
        parser.add_argument('--warranty_start', action='store', default='', help='Set all the values in this column to the given value.')
        parser.add_argument('--warranty_end', action='store', default='', help='Set all the values in this column to the given value.')
        parser.add_argument('--contact_office', action='store', default='', help='Set all the values in this column to the given value.')
        parser.add_argument('--fund_type', action='store', default='', help='Set all the values in this column to the given value.')
        parser.add_argument('--floor', action='store', default='', help='Set all the values in this column to the given value.')
        parser.add_argument('--office', action='store', default='', help='Set all the values in this column to the given value. Office for the tbl_asset_location')
        parser.add_argument('--purch_date', action='store', default='', help='Set all the values in this column to the given value.')

        args = parser.parse_args()

        self.args = args

    @property
    def path_to_file(self):
        return self.args.f_name
    
    @property
    def owner(self):
        return self.args.owner
    
    @property
    def room(self):
        return self.args.room

    @property
    def asset_desc(self):
        return self.args.asset_desc

    @property
    def serial_num(self):
        return self.args.serial_num

    @property
    def po_num(self):
        return self.args.po_num

    @property
    def contact_phone(self):
        return self.args.contact_phone

    @property
    def contact_ext(self):
        return self.args.contact_ext

    @property
    def department(self):
        return self.args.department

    @property
    def contact_office(self):
        return self.args.contact_office

    @property
    def warranty_num(self):
        return self.args.warranty_num

    @property
    def warranty_start(self):
        return self.args.warranty_start

    @property
    def warranty_end(self):
        return self.args.warranty_end

    @property
    def fund_type(self):
        return self.args.fund_type

    @property
    def floor(self):
        return self.args.floor

    @property
    def office(self):
        return self.args.office

    @property
    def purch_date(self):
        return self.args.purch_date
    
    def __str__(self):
        return f"{self.args}"