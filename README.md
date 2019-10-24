# csvTransform

## Program Description

csvTransform is a program that modifies csv files obtained from the oracle database to match the inventaries database. It is important to run this program on a csv obtained from oracle before drag and dropping it in the dropzone.

## Installation
```
pip3 install -e git://github.com/catecupr/csvTransform.git#egg=csvTransform.egg-info
```

To uninstall run:
```
pip3 uninstall csvTransform
```

## Usage

#### Command in Terminal

```
csvTransform --f_name={Path to file} [Flags]
```

Example: 
```
csvTransform --f_name=~/path/to/csv_to_transform.csv --owner=john.smith6@gmail.com
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