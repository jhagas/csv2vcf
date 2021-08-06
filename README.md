# CSV To VCF
Python script to convert CSV data to VCF contact file format
> Bagi MABA, script ini bisa digunakan untuk secara otomatis menyimpan nomor teman seangkatan jika kating kalian meminta kalian melakukan itu. Ckhhhss

## Dependencies
This is a python script with ONLY built-in modules. Make sure you have `python v3.9` installed to your system. You can use this script on all platforms.

## CSV Format
You can see [examples](./formatting.csv) for the format of the CSV. You can empty some entry if you want to.
~[csv example](./screenshot/formatting.png)

## How to use
I assume you have installed `python v3.9` and `git` in your system.

1. Clone this repository
```
git clone https://github.com/jhagas/csv2vcf
cd csv2vcf
```

2. Running this script

- Type the following command and hit ENTER:
```
python csv2vcf.py
```
You have to fill the form correctly, and type `done` and `ENTER` if you are done typing all csv that you want to convert.

- Another way to run this script is to write all CSV file as argument. For example
```
python csv2vcf.py file.csv file2.csv and so on..
```

3. Output file will be saved in folder named `output`

## License
MIT License
