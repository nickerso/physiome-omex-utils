# Utilities for working with OMEX Archive files at the Physiome journal

Prerequisites:

```commandline
$> pip install -r requirements.txt
```

Suggest that you use a Python virtual environment to avoid contaminating your system Python.

## `create_omex_archive.py`

Will create an OMEX Archive for using the given top-level folder. Only the file types that we know about will be included in the generated archive.

```commandline
$> python create_omex_archive.py
usage: python create_omex_archive.py <root-folder> <archive-filename>
       root-folder: the top-level folder to use as the root of the archive
       archive-filename: the name of the OMEX Archive file to create

Supported file types:
   .cellml with MIME type: http://identifiers.org/combine.specifications/cellml
   .sedml with MIME type: http://identifiers.org/combine.specifications/sed-ml
   .py with MIME type: application/x-python
   .csv with MIME type: text/csv
   .m with MIME type: text/x-matlab
   .mat with MIME type: text/x-matlab
   .xlsx with MIME type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
   .pdf with MIME type: application/pdf
   .rst with MIME type: text/x-rst
   .txt with MIME type: text/plain
   .md with MIME type: text/markdown
   .png with MIME type: image/png
   .jpeg with MIME type: image/jpeg
   .jpg with MIME type: image/jpeg
   .html with MIME type: text/html
   .json with MIME type: application/json
```

## `validate_combine_archive.py`

Basic validation of a given OMEX Archive file.

```commandline
$> python validate_combine_archive.py
usage: python validate_combine_archive.py <OMEX File>
```
