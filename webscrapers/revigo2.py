import mechanize

br = mechanize.Browser()
br.open("http://revigo.irb.hr/")
br.select_form(name="aspnetForm")
br["ctl00$MasterContent$txtGOInput"] = ""
txt = open("/home/david/Documents/BenoitLab/RNA-seq/Gprofiler/downDeet.csv").read()
response = br.submit()

with open("test.html", "wb") as f:
    f.write(response.read())
for form in br.forms():
    print("Form name:", form.name)
    for i in form:
        print(i)
