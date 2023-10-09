# Create a manifest file for an omex archive.
# Specify the path of the contents (i.e. the parent directory)
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
import sys
import libcombine
#import lxml.etree as ET

_supported_file_types = {
    ".cellml": "http://identifiers.org/combine.specifications/cellml",
    ".sedml": "http://identifiers.org/combine.specifications/sed-ml",
    ".py": "application/x-python",
    ".csv": "text/csv",
    ".m": "text/x-matlab",
    ".mat": "text/x-matlab",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".pdf": "application/pdf",
    ".rst": "text/x-rst",
    ".txt": "text/plain",
    ".md": "text/markdown",
    ".png": "image/png",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".html": "text/html",
    ".json": "application/json"
}

def known_file_type(file):
    filename, file_ext = os.path.splitext(file)
    if file_ext in _supported_file_types.keys():
        return True
    return False

def get_file_type(file):
    filename, file_ext = os.path.splitext(file)
    if file_ext in _supported_file_types.keys():
        return _supported_file_types[file_ext]
    return ""

def build_manifest(root_dir):
    manifest = libcombine.CaOmexManifest()
    archive = libcombine.CombineArchive()

    # path must end with '/'
    if not root_dir[-1] == '/':
        root_dir += '/'

    # also check subfolders
    f = [os.path.join(dp.split(root_dir)[-1], f).replace('\\', '/') for
         dp, dn, filenames in os.walk(root_dir) for f in filenames]
    f = [i for i in f if not i.endswith('manifest.xml')]
    f = [i for i in f if not i.endswith('.gitignore')]
    f = [i for i in f if known_file_type(i)]
    for i in f:
        content = manifest.createContent()
        content.setLocation(i)
        content.setFormat(get_file_type(i))
        archive.addFile(
            i, # file to add
            i, # filename in the archive
            get_file_type(i), # file type
            False # master file
        )

    archive.writeToFile("test.omex")

    # add the archive itself and the manifest
    content = manifest.createContent()
    content.setLocation('.')
    content.setFormat('https://identifiers.org/combine.specifications/omex')
    content = manifest.createContent()
    content.setLocation('./manifest.xml')
    content.setFormat('https://identifiers.org/combine.specifications/omex-manifest')

    return libcombine.writeOMEXToString(manifest)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python omex_manifest_maker.py <root-folder>")
        print("\nSupported file types:")
        for ext in _supported_file_types:
            print("   {0} with MIME type: {1}".format(ext, _supported_file_types[ext]))
        sys.exit(1)

    manifest_string = build_manifest(sys.argv[1])
    print(manifest_string)
