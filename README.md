# AppManipulator

This is a basic Python Script to Manipulate and Repackage Android App Packages in an Automated Way


## Dependencies
AppManipulator requires
- apktool to disassemble and re-assemble APK packages
- jarsigner to sign again the repackaged APK

It also requires a signing certificate to be present at the working directory in order to succesfully sign the apk. Users must first run the command shown below to create required signing certificate, keystore and alias
```sh
keytool -genkey -v -keystore testkeystore -keyalg RSA -keysize 2048 -storepass testtest -validity 3650 -alias testkey
```

## Usage
```sh
python appmanipulator.py -i INPUT_APK -o OUTPUT_APK -f FILE_TO_BE_MANIPULATED -s STRING_TO_SEARCH -r STRING_TO_REPLACE
```
