# Utilities for working with OMEX Archive files at the Physiome journal

Prerequisites:

```commandline
$> uv sync
```

The project is configured for uv. Running `uv sync` creates and manages the local virtual environment automatically.

You can run commands from inside the source folder, or from anywhere by pointing uv to this project with `--project`.

## `create_omex_archive.py`

Will create an OMEX Archive for using the given top-level folder. Only the file types that we know about will be included in the generated archive.

```commandline
$> uv run create-omex-archive
usage: create-omex-archive <root-folder> <archive-filename>
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

Run from another folder (for example, where your submission files live):

```commandline
$> uv run --project C:\path\to\physiome-omex-utils create-omex-archive .\MySubmission MySubmission.omex
```

## `validate_combine_archive.py`

Basic validation of a given OMEX Archive file.

```commandline
$> uv run validate-combine-archive
usage: validate-combine-archive <OMEX File>
```

Run from another folder:

```commandline
$> uv run --project C:\path\to\physiome-omex-utils validate-combine-archive .\MySubmission.omex
```

## Quick examples (copy/paste)

Use these commands with a real submission folder called `S000007`.

From inside this repository:

```commandline
$> uv run create-omex-archive .\submission_files\S000007 .\submission_files\S000007.omex
$> uv run validate-combine-archive .\submission_files\S000007.omex
```

From anywhere (outside this repository):

```commandline
$> uv run --project C:\path\to\physiome-omex-utils create-omex-archive C:\path\to\my\files\S000007 C:\path\to\my\files\S000007.omex
$> uv run --project C:\path\to\physiome-omex-utils validate-combine-archive C:\path\to\my\files\S000007.omex
```
