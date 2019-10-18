# csvTransform
Example (1): 
```
csvTransform --f_name=~/Desktop/CSVs/csv_to_transform.csv --owner=joel.ruiz6@upr.edu
```

Example (2):
```
python __main__.py --f_name='/home/catec/Desktop/CSVs/ADM_PLANTA_FISICA.csv' --owner=Nolo@upr.edu
```

## Program Description

csvTransform is a program that modifies csv files obtained from the oracle database to match the inventaries database. It is important to run this program on a csv obtained from oracle before drag and dropping it in the dropzone.

## Usage

#### Command in Terminal

```
csvTransform --f_name={Path to file} [Flags]
```

#### Flags and Arguments
    The flags are a set of column names that you can use to modify the value for an entire column. For example:
    using the argument --owner=Nolo@upr.edu will make every value in the column owner to be Nolo@upr.edu.
##### Required arguments (Needed for the program to run):
    --f_name 

##### Optional arguments:
    Not using the following arguments will leave the columns as they are in the csv.

    --owner
    --room
    --asset_desc
    --serial_num
    --po_num

    Not using the following arguments will create the columns with an empty string as a default value.

    --contact_phone
    --contact_ext
    --department
    --warranty_num
    --warranty_start
    --warranty_end
    --contact_office
    --fund_type
    --floor
    --office
    --purch_date