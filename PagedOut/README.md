<!-- pandoc -s -f gfm -t html README.md -o README.html -->

- [Adding any external data to any PDF](#adding-any-external-data-to-any-pdf)
  - [Attaching](#attaching)
  - [Incremental updates](#incremental-updates)
  - [Incompatibilities with polyglots](#incompatibilities-with-polyglots)
    - [Absolute offsets](#absolute-offsets)
    - [Embedding by hand](#embedding-by-hand)
    - [Appended data](#appended-data)
- [Conclusion](#conclusion)
- [PoCs](#pocs)


# Adding any external data to any PDF

Goals:
- embed elegantly any data in a PDF.
- making a ZIP/PDF polyglot with maximum compatibility

A shorter version of this article appeared in [PagedOut!](https://pagedout.institute) #1, page 16.


## Attaching

To attach a file to a PDF, you can rely on free tools out there:

```
pdftk doc.pdf attach_files myfile.bin output attached.pdf
```

Note that Adobe Reader forbids to download EXE, VBS or ZIP files,
so you might want to rename their extensions.

When attaching such files, the entire file is recreated,
so you can't revert to the original doc.

## Incremental updates

A more elegant way to attach a file is to do it via an incremental update,
so that you make it clear that the file was attached afterwards:
the original file body is unmodified,
only the updating or new elements will be appended to it:
an XREF (cross reference table) update, a new catalog that references the attachment,
the attachment declaration and its data stream.

Example with PyMuPDF:

``` python
import fitz # from PyMuPDF
...
doc = fitz.open(pdf)
...
# create an attachment
# modify the extension to bypass blacklisting
doc.embeddedFileAdd(name,
    data, name, name + "_")
# save incrementally
doc.saveIncr()
```

This script may look really simple,
but it will handle for you complex cases such as
linearization, object streams or classic xrefs,
will only append new or updated objects
and leave the original file body intact,
and will give back a perfectly valid PDF file.

That said, if you attach a ZIP to a PDF,
you could think of making it a ZIP/PDF polyglot.


## Incompatibilities with polyglots
But these are mutually exclusive:
even if you store the incremental update with no compression via

`doc.save(doc.name, incremental=True, expand=255)`,

some incompatibilities will remain.

### Absolute offsets
To be perfectly compatible
(for example with *7z* or *Windows Explorer*)
a ZIP archive needs its offset to be re-adjusted
so that they are absolute to the *file*,
not relative to the start of the *archive*
(where the ZIP structure start).

If it's the case, you will get such warnings with these files:

```
$ unzip -v test.pdf
...
warning [test.pdf]:  533 extra bytes at beginning or within zipfile
  (attempting to process anyway)
...
```

```
$ zip -T test.pdf
        zip warning: unexpected signature on disk 0 at 533

        zip warning: archive not in correct format: test.pdf
        zip warning: (try -F to attempt recovery)
```

This can be fixed in place with the Info-ZIP `zip -F` command.

But then when you extract the Zip as a PDF attachment,
its offsets will be incorrect again,
as only the attachment will be copied out of the file.

### Embedding by hand

So you may want to drop the attachment functionality altogether,
and just embed the file as a single data stream instead.

``` python
# create a dummy object entry
objNb = doc._getNewXref()
doc._updateObject(objNb, '<<>>')

# add contents of the archive
doc._updateStream(objNb, zipdata, new=True)
```

### Appended data

Some tools will still complain that there is appended data after the archive
when you read it inside from the polyglot.

```
$ 7za t test.pdf

[...]
Testing archive: test.pdf

WARNINGS:
There are data after the end of archive

--
Path = test.pdf
Type = zip
WARNINGS:
There are data after the end of archive
Offset = 387031
Physical Size = 392734
Tail Size = 231
[...]

```

A workaround is to extend the archive comment
to the end of the file
once it's in the polyglot:

``` python
# locating the comment length in the ZIP's EoCD
# 4:Sig  2:NbDisk 2: NbCD 2:TotalDisk 2:TotalCD
# 	4:CDSize 4:Offset 2:ComLen
offset = filedata.rfind("PK\5\6") + 20

# new comment length
length = len(filedata) - offset - 2

with open(pdf, "wb") as f:
	f.write(filedata[:offset])
	f.write(struct.pack("<H", length))
	f.write(filedata[offset+2:])
```

To avoid that archive viewers show an archive comment
that is now full of PDF keywords,
a working trick is to start the comment with a null byte,
which will truncate early the null-terminated comment.

Just append such a byte to the ZIP when reading it,
before adding it to the PDF document:

``` python
# appending one null byte to terminate the archive comment
with open(zip_, 'rb') as f:
	zipdata = f.read() + "\0"
```

If you don't, some operations on the archive will unexpectedly list PDF contents
because the tools just dump the comments contents.

```
$ unzip -v test.pdf
Archive:  test.pdf

endstream
endobj

xref
891 1
0000386995 00000 n

trailer
<</Size 892/Info 889 0 R/Root 888 0 R/ID[(\031\314G\265*U\255,\021\261\360\)\255\357"q)(\031\314G\265*U\255,\021\261\360\)\255\357"q)]/Prev 369018>>
startxref
779784
%%EOF
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
      12  Defl:X       14 -17% 07/28/2019 23:31 1c291ca3  hello.txt
--------          -------  ---                            -------
      12               14 -17%                            1 file
```


# Conclusion

Attaching a file via an incremental update
is an elegant way to extend a document while preserving its original structure.
But a ZIP file can't be at the same time attached to a PDF doc and
referenced externally as a ZIP/PDF polyglot, while keeping maximum compatibility.

Ange Albertini with Nicolas Grégoire, Gynvael Coldwind and Philippe Teuwen for their help,

# PoCs

A [script](make_pdf.py) to rely on PyMuPDF to do an incremental update to any kind of PDF.

PoCs
- [standard](standard.pdf)
- [linearized](linearized.pdf)
- [object streams](objectstreams.pdf)
