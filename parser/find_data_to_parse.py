import glob

CORPUS_LOCATION = "/Volumes/bigone/lensdata/contracts"

glob_files = glob.glob(CORPUS_LOCATION + "/*_text.txt")

print len(glob_files)