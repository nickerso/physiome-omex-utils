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

path = "C:/Users/sfon036/Desktop/work_files/PhysiomeSubmissions/s000014_prepublish/model_files" # "submission_files/S000007/"
path = "C:/Users/sfon036/OneDrive - The University of Auckland/physiome_curation_work/DL_models/Noroozbabaee2022PhysiomeS000015"

# path must end with '/'
if not path[-1] == '/':
    path += '/'

# also check subfolders
f = [os.path.join(dp.split(path)[-1], f).replace('\\','/') for dp, dn, filenames in os.walk(path) for f in filenames]
# f = os.listdir(path)
f = [i for i in f if not i.endswith('manifest.xml')]
f = [i for i in f if not i.endswith('.gitignore')]
f = [i.lower() for i in f]

f_all = dict()

f_all['clml'] = [i for i in f if i.endswith(".cellml")]
f_all['sed'] = [i for i in f if i.endswith(".sedml")]
f_all['py'] = [i for i in f if i.endswith(".py")]
f_all['csv'] = [i for i in f if i.endswith(".csv")]
f_all['mat'] = [i for i in f if i.endswith(".m")]
f_all['xlsx'] = [i for i in f if i.endswith(".xlsx")]
f_all['pdf'] = [i for i in f if i.endswith(".pdf")]
f_all['rst'] = [i for i in f if i.endswith(".rst")]
f_all['txt'] = [i for i in f if i.endswith(".txt")]
f_all['md'] = [i for i in f if i.endswith(".md")]
f_all['png'] = [i for i in f if i.endswith(".png")]
f_all['jpeg'] = [i for i in f if i.endswith(".jpeg") and i.endswith(".jpg")]
f_all['html'] = [i for i in f if i.endswith(".html")]
f_all['json'] = [i for i in f if i.endswith(".json")]

# fcopy = f_all.copy()
# allk = fcopy.keys()
# for k in allk:
#     if f_all[k] == []:
#         del f_all[k]
# check if any MIME type (suffix) is not accounted for
# flat = [i for f_all[fkey] in f_all for i in f_all[fkey]]
flat = []
for fkey in f_all:
    flat += f_all[fkey]
assert len(flat) == len(f)

# write to manifest
outfile = path + "manifest.xml"
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
    if cname in f_all['clml']:
        contentx.set("format", "http://identifiers.org/combine.specifications/cellml")
    if cname in f_all['sed']:
        contentx.set("format", "http://identifiers.org/combine.specifications/sed-ml")
    if cname in f_all['py']:
        contentx.set("format", "application/x-python")
    if cname in f_all['csv']:
        contentx.set("format", "text/csv")
    if cname in f_all['mat']:
        contentx.set("format", "text/x-matlab")
    if cname in f_all['xlsx']:
        contentx.set("format", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    if cname in f_all['pdf']:
        contentx.set("format", "application/pdf")
    if cname in f_all['rst']:
        contentx.set("format", "text/x-rst")
    if cname in f_all['txt']:
        contentx.set("format", "text/plain")
    if cname in f_all['md']:
        contentx.set("format", "text/markdown")
    if cname in f_all['png']:
        contentx.set("format", "image/png")
    if cname in f_all['jpeg']:
        contentx.set("format", "image/jpeg")
    if cname in f_all['html']:
        contentx.set("format", "text/html")
    if cname in f_all['json']:
        contentx.set("format", "application/json")

tree = ET.ElementTree(data)
tree.write(outfile, encoding="utf-8", xml_declaration=True, pretty_print=True)
