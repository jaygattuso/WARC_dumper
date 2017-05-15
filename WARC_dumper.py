import os
from warcio.archiveiterator import ArchiveIterator

#### full path to warc file here
warc_file = r"my_warc_file.warc.gz"

#### full path to unpack location 
#### creates two sub folders, media_dump and file_dump
#### files that match the given extensions go to the "media_dump" subfolder
#### otherwise, files go to "files_dump". Doesn't try very hard... 
destination = r"C:\\my_project\file_dump"

################################################################################################

if not os.path.exists(os.path.join(destination, file_dump)):
	os.makedir(os.path.join(destination, file_dump))

if not os.path.exists(os.path.join(destination, media_dump)):
	os.makedir(os.path.join(destination, media_dump))	

with open(warc_file, 'rb') as stream:
	for record in ArchiveIterator(stream):
		if record.rec_type == 'response':
			__, fname = record.rec_headers.get_header("WARC-Target-URI").rsplit("/", 1)
			if fname.endswith(".jpg") or fname.endswith(".mp4") or fname.endswith(".png") or fname.endswith(".pdf"):
				with open(os.path.join(media_dump, fname), "wb") as data:
					data.write(record.content_stream().read())
			else:
				try:
					with open(os.path.join(file_dump, fname), "wb") as data:
						data.write(record.content_stream().read())
				except:
					print "Failed to write binary for: {}".format(record.rec_headers.get_header("WARC-Target-URI")) 
