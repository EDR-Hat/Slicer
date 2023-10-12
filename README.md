# Slicer
Python script that copies out portions of video automatically from a file, using a text file
Currently it is only set to copy mode, it won't reencode video at all. Will set a flag option for that in the future.

Format the text file you use by having the directory name you want on a line and then any number of clip timestamps following each on their own line. You can have multiple directories for a file, just do an empty newline between directories.
Take a look at the example file 0.txt that puts a bunch of clips into "Ads" and "News" directories.
