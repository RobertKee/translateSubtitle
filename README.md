This script creates a new subtitle file, translating lines with google translate. It is meant to run on the command line.
The extension will be set to `.<destination_language>.<extension>`, e.g. `.en.srt`

to install:
run the build script in the root directory `./build.sh`

to run:
`subtitleTranslate --file <full_file_path>`

optional arguments 
`--source_lang` <lang_code>
`--dest_lang` <lang_code>

These args are optional, specifying `source_lang` will help with accuracy but is not required.
Specifying `dest_lang` is only needed if the desired output is different than the system standard language.

The full list of supported languages can be found here: 
https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages