# Create a manifest file for an omex archive. Specify the path of the contents (i.e. the parent directory)
# Output: new_manifest.xml (rename to manifest.xml before putting into OMEX archive)
# Author: Shelley Fong

# list of supported MIME types:
# .cellml
# .sedml
# .python
# .csv
# .m
# .xlsx
# .pdf
# Fork this repository then do a git pull request to add new MIME types or to make changes.

import os
import lxml.etree as ET

path = "C:/Users/sfon036/Desktop/work_files/PhysiomeSubmissions/Ai2021PhysiomeS000013_27Oct/" # "submission_files/S000007/"

# also check subfolders
f = [os.path.join(dp.split(path)[-1], f).replace('\\','/') for dp, dn, filenames in os.walk(path) for f in filenames]
# f = os.listdir(path)
f = [i for i in f if not i.endswith('manifest.xml')]

fclml = [i for i in f if i.endswith(".cellml")]
fsed = [i for i in f if i.endswith(".sedml")]
fpy = [i for i in f if i.endswith(".py")]
fcsv = [i for i in f if i.endswith(".csv")]
fmat = [i for i in f if i.endswith(".m")]
fxlsx = [i for i in f if i.endswith(".xlsx")]
fpdf = [i for i in f if i.endswith(".pdf")]

# check if any MIME type (suffix) is not accounted for
assert len(fclml + fsed + fpy + fcsv + fmat + fxlsx + fpdf) == len(f), "Filetype present which not on list of supported MIME types"

# write to manifest
outfile = path + "new_manifest.xml"
data = ET.Element("omexManifest")
data.set("xmlns","https://identifiers.org/combine.specifications/omex-manifest")
content = ET.SubElement(data, "content")
content2 = ET.SubElement(data, "content")
content.set("location", ".")
content.set("format", "https://identifiers.org/combine.specifications/omex")
content2.set("location", "./manifest.xml")
content2.set("format", "https://identifiers.org/combine.specifications/omex-manifest")

# write out cellml files followed by sedml files etc
for cname in f:
    contentx = ET.SubElement(data, "content")
    contentx.set("location", "./" + cname)
    if cname in fclml:
        contentx.set("format", "http://identifiers.org/combine.specifications/cellml")
    if cname in fsed:
        contentx.set("format", "http://identifiers.org/combine.specifications/sed-ml")
    if cname in fpy:
        contentx.set("format", "application/x-python")
    if cname in fcsv:
        contentx.set("format", "text/csv")
    if cname in fmat:
        contentx.set("format", "text/x-matlab")
    if cname in fxlsx:
        contentx.set("format", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    if cname in fpdf:
        contentx.set("format", "application/pdf")

tree = ET.ElementTree(data)
tree.write(outfile, encoding="utf-8", xml_declaration=True, pretty_print=True)
