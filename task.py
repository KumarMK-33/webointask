# import csv

# def load_data(filename):
#     my_list=[]
#     with open(filename) as data:
#         name_data= csv.reader(data, delimiter=',')
#         next(name_data)
#         for row in name_data:
#             my_list.append(row)
#         return my_list
    
# new_list = load_data('All Bills.csv')
# for row in new_list:
#     print(row)

import csv
import pdfkit
from jinja2 import Template

def load_data(filename):
    data_list = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        for _ in range(29):
            next(reader, None)
            
        for row in reader:
            data_list.append(row)
    return data_list

def render_html(row_data):
    with open('template.html', 'r') as file:
        html_template = file.read()
    template = Template(html_template)
    return template.render(row_data=row_data)


path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' 

config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

def convert_html_to_pdf(html_content, output_filename):
    pdfkit.from_string(html_content, output_filename, configuration=config)


# Main execution
csv_file = 'All Bills.csv'
data = load_data(csv_file)

start_index = 30
end_index = 33

for index, row in enumerate(data[start_index:end_index], start=start_index):
    html_content = render_html(row)
    output_filename = f"invoice_{index}.pdf"
    convert_html_to_pdf(html_content, output_filename)
    print(f"PDF generated: {output_filename}")
