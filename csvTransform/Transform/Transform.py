import pandas as pd

class Transform:

    @classmethod
    def oracleDB_to_inventariesDB(cls, args, csv_data):
        cls.__alter_column_values(args, csv_data)
        cls.__add_missing_columns(args, csv_data)
        cls.__change_column_names(csv_data)
        cls.__normalize_location_column(csv_data)
        cls.__format_tag_num_column(csv_data)

        # Change all the cell that contain estatal to Institutional
        for i, value in enumerate(csv_data['Fund Type']):
            if value.lower() == 'estatal':
                csv_data['Fund Type'][i] = 'Institutional'

        cls.__delete_unused_columns(csv_data)


    @staticmethod
    def __alter_column_values(args, csv_data):
        
        if args.owner != None:
            csv_data['Owner'] = args.owner

        if args.room != None:
            csv_data['Room'] = args.room

        if args.asset_desc != None:
            csv_data['Asset Description'] = args.asset_desc

        if args.serial_num != None:
            csv_data['Serial'] = args.serial_num

        if args.po_num != None:
            csv_data['PO Number'] = args.po_num


    @staticmethod
    def __add_missing_columns(args, csv_data):
        csv_data['Contact Name'] = csv_data['Owner']
        csv_data['Contact Phone'] = args.contact_phone
        csv_data['Contact Extension'] = args.contact_ext
        csv_data['Contact Office'] = args.contact_office
        csv_data['Department'] = args.department
        csv_data['Warranty Number'] = args.warranty_num
        csv_data['Warranty Start'] = args.warranty_start
        csv_data['Warranty End'] = args.warranty_end
        csv_data['Floor'] = args.fund_type
        csv_data['Office'] = args.office
        csv_data['Purchase Date'] = args.purch_date
        

    @staticmethod
    def __change_column_names(csv_data):
        csv_data.rename(columns={'Room': 'Location Description',
                                 'Cost': 'Purchase Cost',
                                 'Owner': 'Assigned Person',
                                 'Origen Fondo': 'Fund Type'}, inplace=True)


    @staticmethod
    def __normalize_location_column(csv_data):

        # Example of a value in csv_data['Location'] --> '020-0022-100-01'
        # 020 is the Campus
        # 0022 is the Building (20022 in inventaries and 0022 in Oracle)
        # 100 is the office number
        # 01 is the state (PR)
        csv_data['Campus'] = ''
        csv_data['Building'] = ''
        csv_data['Office Number'] = ''

        for i, cell in enumerate(csv_data['Location']):
            campus, building, office_num, state = cell.split('-')
            
            if campus == '020':
                csv_data['Campus'][i] = 'Recinto de Río Piedras'

            csv_data['Building'][i] = campus[1] + building
            csv_data['Office Number'][i] = office_num


    @staticmethod
    def __delete_unused_columns(csv_data):
        del csv_data['Cost Account']
        del csv_data['Units']
        del csv_data['Asset Type']
        del csv_data['Fondo']
        del csv_data['Asset Key']
        del csv_data['Location']


    @staticmethod
    def __format_tag_num_column(csv_data):

        for i, cell in enumerate(csv_data['Tag Number']):
            campus, tag_number = cell.split('-')
            csv_data['Tag Number'][i] = tag_number