#%%
import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser
import re
import os
import pandas as pd


def autoRevigo(name):
    name = name
    os.chdir("/home/david/Documents/BenoitLab/RNA-seq/Gprofiler/")
    os.listdir(".")
    file = open(name, "r")

    string = ""

    for line in file.readlines():
        # print(line)
        string = string + line + "\n"

    goterms = string

    br = RoboBrowser(parser="html")
    br.open("http://revigo.irb.hr/")

    form = br.get_form()
    form["goList"].value = goterms

    br.submit_form(form)

    download_rsc_link = br.find("a", href=re.compile("toR.jsp"))
    br.follow_link(download_rsc_link)
    r_code = br.response.content.decode("utf-8")
    print(r_code)

    br.back()

    download_csv_link = br.find("a", href=re.compile("export.jsp"))
    br.follow_link(download_csv_link)
    csv_content = br.response.content.decode("utf-8")

    writefile = open("/home/david/Documents/BenoitLab/RNA-seq/Revigo/" + name, "w")

    writefile.write(csv_content)
    writefile.close()


# %%
import glob

os.chdir("/home/david/Documents/BenoitLab/RNA-seq/Gprofiler/")
for i in glob.glob("*.csv"):
    autoRevigo(i)
