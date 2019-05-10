from pyexcel_ods3 import get_data, save_data
import json

def importods(inp, outp):
    data = get_data(inp, encoding="utf-8")
    sheets = {}
    headers = ["Datum", "Vorname", "Nachname", "Strasse", "Hausnummer", "PLZ", "Stadt", "Telefon", "Code"]
    #print(json.dumps(data))
    for key in data.keys():
        #print("key:", key)
        val1 = data.get(key)
        #print("val1:", val1)
        for l1 in val1:
            #print("  l1:", l1)
            if len(l1) == 0 or l1[0] == "Datum":
                continue
            datum = l1[0][0:10]
            if not datum in sheets:
                sheets[datum] = []
            l1 = l1[0:8]  # Datum - Telefon
            l1.append("") # add empty code value
            sheets[datum].append(l1)
    #print("sheets1", sheets)
    for datum in sheets.keys():
        sheets[datum].sort(key = lambda l1: l1[0])
        sheets[datum].insert(0, headers)
    #print("sheets2", sheets)
    #print(json.dumps(sheets, indent=4))
    save_data(outp, sheets, encoding="utf-8")

importods("C:/Users/Michael/Downloads/codiertermine (4).ods", "result.ods")