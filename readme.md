# adb pull-a-lot

Simply and quickly create individualized backups of the internal memory of an Android phone via adb.

## Description

Every now and then I come across the problem that need a simple backup of the internal storage of phones from friends or acquaintances - be it because of a defective display, questionable software update ideas, or just to make sure, because you never know.
I have little confidence in copying via GUI, as it has happened too often that things have gone wrong or simply taken much more time than equivalent operations via the command line.
**adb pull-a-lot** let's you quickly and conveniently define what to exclude from a pull of the _/sdcard_, where to pull it and then simply gets the job done.

## Getting Started

### Dependencies

- Python 3
- adb drivers for your machine
- an android phone with activated adb
- pure-python-adb

```
pip install pure-python-adb
```

### Executing program

- check the config.json

  - **maxdepth** determines the length of paths
  - **exclude** specifies foldernames, filenames or filetypes to be excluded and accepts wildcards(\*)
  - **paths** specifies filepath patterns that will be excluded

- simply execute adb_pull_everything.py your favorite way and chose a target destination for your files

## Help

Tech-savvy people should have no problems to get this up and running.
If you've never heard of adb this script may not be the right choice for you, though.

## Version History

- Initial Release
