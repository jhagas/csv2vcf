import csv
import sys, os, shutil

def convert(filename):
    try:
        datahand = open(filename, "r")
    except:
        print("ERROR: Could not open", filename)
        exit()


    outputfile = filename[:filename.find(".csv")] + ".vcf"
    outputfile = os.path.join(newpath, outputfile)
    outhand = open(outputfile, "a")
    
    csvparse = csv.DictReader(datahand)
    
    for line in csvparse:
        firstname = line["firstname"]
        lastname = line["lastname"]

        fullname = firstname + ' ' + lastname
        fullname = fullname.rstrip()

        cell = line["cell"]
        home = line["home"]
        email = line["email"]
    
        vcfname = f"""BEGIN:VCARD
VERSION:3.0
N:{lastname};{firstname};;;
FN:{fullname}\n"""
        outhand.write(vcfname)

        if cell != '':
            outhand.write(f"TEL;type=CELL:{cell}\n")
        if home != '':
            outhand.write(f"TEL;type=HOME:{home}\n")
        if email != '':
            outhand.write(f"EMAIL;type=INTERNET;type=CELL;type=pref:{email}\n")
        outhand.write("END:VCARD\n")
    

newpath = os.path.join("output")
if not os.path.exists(newpath):
    os.makedirs(newpath)
else:
    shutil.rmtree(newpath)
    os.makedirs(newpath)

if len(sys.argv) == 1:
    file = []
    while True:
        form = input("Select a CSV file (type done to start converting): ")
        if form == "done":
            break
        else:
            file.append(form)

    for __name__ in file:
        convert(__name__)
else:
    file = sys.argv[1:]
    for __name__ in file:
        convert(__name__)

