import pdfkit

path_wkhtmltopdf = r'wkhtmltox/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdf = pdfkit.from_file('templates/login.html', 'out.pdf', configuration=config)
file = open("test.pdf","wb")
file.write(pdf)
file.close()
