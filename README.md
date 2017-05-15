# WARC_dumper
Rudimentary dumper of WARC files via the python warcio lib

This is a very basic script. 

You need to two things. 

A valid WARC file (and its full system path)

A system path for where you want to resulting files to go. 
_________________________________________________________________

You give it a WARC file and it tries to extract all the binaries into one of two folders. 

filename is pulled from `record.rec_headers.get_header('WARC-Target-URI')`


media_dump is where any file that loks like it ends with [.jpg, .pdf, .png, .mp4] 
(add your own to suit). 

file_dump is where everything else goes. Tries to go.... If record.rec_headers.get_header('WARC-Target-URI') results in a bad filename (length, characters etc) then the file doesn't get written, this is logged on screen. 
