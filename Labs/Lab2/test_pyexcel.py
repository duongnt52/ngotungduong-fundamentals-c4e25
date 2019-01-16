import pyexcel
from collections import OrderedDict

list_dict = [
    OrderedDict({
        "Name": "Adam",
        "Age": 28
    }),
    OrderedDict({
        "Name": "Beatrice",
        "Age": 29
    }),
    OrderedDict({
        "Name": "Ceri",
        "Age": 30
    }),
    OrderedDict({
        "Name": "Dean",
        "Age": 26
    })
]
pyexcel.save_as(records = list_dict, dest_file_name = "test.xls" )