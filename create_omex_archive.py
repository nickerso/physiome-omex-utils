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
    else:
        return "unknown"
    return ""

def build_archive(root_dir):
    archive = libcombine.CombineArchive()

    # path must end with '/'
    if not root_dir[-1] == '/':
        root_dir += '/'
    # also check subfolders
    f = [os.path.join(dp.split(root_dir)[-1], f).replace('\\', '/') for
         dp, dn, filenames in os.walk(root_dir) for f in filenames]
    # only keep the file types that we know about
    known_files = []
    unknown_files = []
    for i in f:
        if known_file_type(i):
            known_files.append(i)
        else:
            print("==> Found unknown file type: {}".format(i))
            unknown_files.append(i)
    for i in known_files + unknown_files:
        archive.addFile(
            i, # file to add
            i, # filename in the archive
            get_file_type(i), # file type
            False # master file
        )

    return archive

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python create_omex_archive.py <root-folder> <archive-filename>")
        print("       root-folder: the top-level folder to use as the root of the archive")
        print("       archive-filename: the name of the OMEX Archive file to create")
        print("\nSupported file types:")
        for ext in _supported_file_types:
            print("   {0} with MIME type: {1}".format(ext, _supported_file_types[ext]))
        sys.exit(1)

    archive = build_archive(sys.argv[1])
    archive.writeToFile(sys.argv[2])
