##Cree un programa que use una lista para eliminar keys de un diccionario.


key_list = ["founded_on", "employee_count"]

new_dict = {
    "company_name":"Experian",
    "revenue":"four_billions", 
    "CEO_name":"brian_cassin",
    "founded_on":1999,
    "business_field":"finance",
    "employee_count": 6000
}

for k in key_list:
    new_dict.pop(k, None)
        



print(new_dict)

