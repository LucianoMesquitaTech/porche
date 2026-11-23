import csv, glob, json
import openpyxl

sheet = openpyxl.load_workbook(glob.glob('*.xlsx')[0], data_only=True).active
rows = list(sheet.values)
headers = rows[0]
fields = {'modelo':'PorscheModelSanitized','ano':'ModelYearSanitized','preco':'SalesPriceSanitized','pagamento':'PayMethodSanitized','cidade':'CitySanitized','estado':'StateSanitized','status':'DeliveryStatusSanitized','data':'SaleDateSanitized'}
data = []
for row in rows[1:]:
    item = {key: row[headers.index(value)] for key, value in fields.items()}
    for key in ('ano','preco'):
        try: item[key] = float(item[key]) if key == 'preco' else int(item[key])
        except (ValueError, TypeError): item[key] = None
    data.append(item)
with open('dados_sanitizados.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields.keys()); writer.writeheader(); writer.writerows(data)
with open('dados.json','w',encoding='utf-8') as f: json.dump(data,f,ensure_ascii=False)
print('Registros:',len(data),'Precos validos:',sum(isinstance(r['preco'],float) for r in data),'Datas invalidas:',sum(r['data']=='INVALID' for r in data))
