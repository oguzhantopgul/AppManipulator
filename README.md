# AppManipulator

This is a basic Python Script to Manipulate and Repackage Android App Packages in an Automated Way


## Dependencies
AppManipulator requires
- apktool to disassemble and assemble APK
- jarsigner to sign again the repackaged APK

## Usage
```sh
python appmanipulator.py -i INPUT_APK -o OUTPUT_FOLDER -f FILE_TO_BE_MANIPULATED -s STRING_TO_SEARCH -r STRING_TO_REPLACE
```
