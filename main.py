import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

pattern_name = (
    r"^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)" r"(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)"
)
subst_name = r"\1\3\10\4\6\9\7\8"
pattern_number = (
    r"(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)"
    r"(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)"
    r"(\d{2})(\s*)(\(*)(доб.)*(.)(\s*)(\d+)*(\)*)"
)
subst_num = r"+7(\4)\8-\11-\14\15\17\18\20"

table_new = list()
for name in contacts_list[:-1]:
    temp = ",".join(name)
    temp = re.sub(pattern_name, subst_name, temp)
    temp = re.sub(pattern_number, subst_num, temp)
    table_list = temp.split(",")
    table_new.append(table_list)
pprint(table_new)

corrected_list = []
contacts_list_length = len(table_new)
pass_record = []

for i in range(contacts_list_length - 1):
    if i in pass_record:
        continue
    contact = table_new[i]
    for j in range(i + 1, len(table_new)):
        if contact[0] == table_new[j][0] and contact[1] == table_new[j][1]:
            pass_record.append(j)
            contact = [
                contact[_] if contact[_] != "" else table_new[j][_]
                for _ in range(len(contact))
            ]
    corrected_list.append(contact)

with open("phonebook.csv", "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(corrected_list)
