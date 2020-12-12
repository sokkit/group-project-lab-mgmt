import pdfkit

path_wkhtmltopdf = r'wkhtmltox/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

options = {
  "enable-local-file-access": None
}

pdf = pdfkit.from_file('templates/HTMLtoPDF.html', 'out.pdf', configuration=config, options=options)
file = open("test.pdf","wb")
file.write(pdf)
file.close()
