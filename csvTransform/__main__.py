import pandas as pd
from .Args.args import Args
from .Transform.Transform import Transform


def main(args=None):

    if args == None:
        args = Args()

    # Read csv and transform it
    csv_data = pd.read_csv(args.path_to_file)

    print('Transforming ...')
    Transform.oracleDB_to_inventariesDB(args, csv_data)

    # Re-order columns
    csv_data = csv_data[['Assigned Person', 'Tag Number', 'PO Number', 'Purchase Cost', 'Purchase Date', 'Fund Type', 'Serial', 'Warranty Number', 'Warranty Start', 'Warranty End', 'Asset Description', 'Contact Name', 'Contact Phone', 'Contact Extension', 'Contact Office', 'Campus', 'Building', 'Department', 'Office Number', 'Floor', 'Office', 'Location Description']]

    # Save csv in current path
    csv_data.to_csv('./result.csv', sep=',', encoding='utf-8', index=False)

    print('Done')


if __name__ == '__main__':
    main()