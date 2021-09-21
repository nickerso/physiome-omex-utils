import os
import lxml.etree as ET

path = "submission_files/Ai2021PhysiomeS000009/"

# also check subfolders
f = [os.path.join(dp.split(path)[-1], f).replace('\\','/') for dp, dn, filenames in os.walk(path) for f in filenames]
# f = os.listdir(path)

fclml = [i for i in f if i.endswith(".cellml")]
fsed = [i for i in f if i.endswith(".sedml")]
fpy = [i for i in f if i.endswith(".py")]
fcsv = [i for i in f if i.endswith(".csv")]
fmat = [i for i in f if i.endswith(".m")]
fxlsx = [i for i in f if i.endswith(".xlsx")]
fpdf = [i for i in f if i.endswith(".pdf")]

# write to manifest
outfile = path + "new_manifest.xml"
if True:
    data = ET.Element("omexManifest")
    data.set("xmlns","https://identifiers.org/combine.specifications/omex-manifest")
    content = ET.SubElement(data, "content")
    content2 = ET.SubElement(data, "content")
    content.set("location", ".")
    content.set("format", "https://identifiers.org/combine.specifications/omex")
    content2.set("location", "./manifest.xml")
    content2.set("format", "https://identifiers.org/combine.specifications/omex-manifest")

    # write out cellml files followed by sedml files
    for cname in fclml:
        contentx = ET.SubElement(data, "content")
        contentx.set("location", "./"+cname)
        contentx.set("format", "http://identifiers.org/combine.specifications/cellml")
    for cname in fsed:
        contentx = ET.SubElement(data, "content")
        contentx.set("location", "./"+cname)
        contentx.set("format", "http://identifiers.org/combine.specifications/sed-ml")
    for cname in fpy:
        contentx = ET.SubElement(data, "content")
        contentx.set("location", "./"+cname)
        contentx.set("format", "application/x-python")
    for cname in fcsv:
        contentx = ET.SubElement(data, "content")
        contentx.set("location", "./"+cname)
        contentx.set("format", "text/csv")
    for cname in fmat:
        contentx = ET.SubElement(data, "content")
        contentx.set("location", "./"+cname)
        contentx.set("format", "text/x-matlab")
    for cname in fxlsx:
        contentx = ET.SubElement(data, "content")
        contentx.set("location", "./"+cname)
        contentx.set("format", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    for cname in fxlsx:
        contentx = ET.SubElement(data, "content")
        contentx.set("location", "./"+cname)
        contentx.set("format", "application/pdf")

    # content.text = "ffffffff"

    tree = ET.ElementTree(data)
    tree.write(outfile, encoding="utf-8", xml_declaration=True, pretty_print=True)
else:
    with open(outfile,"w") as of:
        of.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        of.write('<omexManifest xmlns="https://identifiers.org/combine.specifications/omex-manifest">\n')
        of.write('  <content location="." format="https://identifiers.org/combine.specifications/omex" />\n')
        of.write('  <content location="./manifest.xml" format="https://identifiers.org/combine.specifications/omex-manifest" />\n')

        # write out cellml files followed by sedml files
        for cname in fclml:
            of.write('  <content location="./" + cname + "" format="http://identifiers.org/combine.specifications/cellml" />\n')

        of.close()

j = 10