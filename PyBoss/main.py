import os
import csv
from datetime import datetime


us_state_abbrev = { 
     'Alabama': 'AL', 
     'Alaska': 'AK', 
     'Arizona': 'AZ', 
     'Arkansas': 'AR', 
     'California': 'CA', 
     'Colorado': 'CO', 
     'Connecticut': 'CT', 
     'Delaware': 'DE', 
     'Florida': 'FL', 
     'Georgia': 'GA', 
     'Hawaii': 'HI', 
     'Idaho': 'ID', 
     'Illinois': 'IL', 
     'Indiana': 'IN', 
     'Iowa': 'IA', 
     'Kansas': 'KS', 
     'Kentucky': 'KY', 
     'Louisiana': 'LA', 
     'Maine': 'ME', 
     'Maryland': 'MD', 
     'Massachusetts': 'MA', 
     'Michigan': 'MI', 
     'Minnesota': 'MN', 
     'Mississippi': 'MS', 
     'Missouri': 'MO', 
     'Montana': 'MT', 
     'Nebraska': 'NE', 
     'Nevada': 'NV', 
     'New Hampshire': 'NH', 
     'New Jersey': 'NJ', 
     'New Mexico': 'NM', 
     'New York': 'NY', 
     'North Carolina': 'NC', 
     'North Dakota': 'ND', 
     'Ohio': 'OH', 
     'Oklahoma': 'OK', 
     'Oregon': 'OR', 
     'Pennsylvania': 'PA', 
     'Rhode Island': 'RI', 
     'South Carolina': 'SC', 
     'South Dakota': 'SD', 
     'Tennessee': 'TN', 
     'Texas': 'TX', 
     'Utah': 'UT', 
     'Vermont': 'VT', 
     'Virginia': 'VA', 
     'Washington': 'WA', 
     'West Virginia': 'WV', 
     'Wisconsin': 'WI', 
     'Wyoming': 'WY'
 } 

file_list=['employee_data1.csv', 'employee_data2.csv']

#file_list=['employee_data1.csv','employee_data2.csv']
output_file_path = os.path.join('output', 'employee_data_final.csv')
with open(output_file_path, 'w', newline='') as output_data:
    field_names=['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    dict_writer=csv.DictWriter(output_data,fieldnames=field_names)
    dict_writer.writeheader()

    for data_file in file_list:    
        file_path = os.path.join('raw_data',data_file)
        
        with open(file_path,'r',newline='') as input_data:

            dictReader = csv.DictReader(input_data)
            for record in dictReader:
                w_record = {}
                w_record['Emp ID'] = record['Emp ID']
                full_name = str(record['Name']).split(' ')
                w_record['First Name'] = full_name[0]
                w_record['Last Name'] = full_name[1]

                #date_parts= str(record['DOB']).split('-')
               # rec_date = datetime.date(date_parts[0], date_parts[1], date_parts[2])
                rec_date= datetime.strptime(record['DOB'],'%Y-%m-%d')
                w_record['DOB']=rec_date.strftime('%d/%m/%Y')
                w_record['SSN'] = "***-**-{}".format("".join(str(record['SSN'])[-4:]))
                w_record['State'] = us_state_abbrev[record['State']]
                dict_writer.writerow(w_record)
                print(w_record)
         

