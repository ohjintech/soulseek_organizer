import shutil
import os
from datetime import datetime
from pathlib import Path


def recursive_copy(src, destination, log):
   

    from_path = os.path.join(os.getcwd(), src)
    dest_path = os.path.join(os.getcwd(), destination)

    for f in sorted(os.listdir(from_path)):

      file = os.path.join(src, f)

      if os.path.isfile(file):

          from_file = os.path.join(from_path, f)
          to_file = os.path.join(dest_path, f)

          log.write(f"\t\t{f}\n")
          
          shutil.move(from_file, to_file)

      else:
          recursive_copy(file, destination, log)


def cleanup(path, log):
 
  log.write(f"Cleaning up {path} folder...\n")
  cleanpath = os.path.join(os.getcwd(), path)

  if not os.path.isdir(cleanpath) :
    return 1

  for dir in os.listdir(cleanpath):
    dir_path = os.path.join(cleanpath, dir)
    try:
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)            
    except Exception as e:
        log.write(f'Failed to delete %s. Reason: %s\n' % (dir_path, e))    

def main() :

  today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

  # logfile
  if os.path.isfile('extract_log.txt'):
    logfile = open('extract_log.txt', 'a')
    logExists = True
    
  else:
    logfile =  open('extract_log.txt', 'w')
    logExists = False
  
  logfile.write(f"=====================================================================\n")
  logfile.write(f"================ Extraction date: {today}================\n\n")
  logfile.write(f"Starting extraction: \n\n")

  if logExists:
    logfile.write(f"Appending to logfile.\n")
  else:
    logfile.write('This is the beginning of the extraction logfile. Enjoy! -- jintaco \n')

  if not os.path.isdir('complete'):
    os.mkdir('extracted')
    logfile.write('Extraction folder missing. Creating new...\n')
  else:
    logfile.write(f"Extraction folder already exists. Appending the following files...\n")
  
  # recursively find all files in complete folder
  print("Files and directories in complete: ")
  for dir in os.listdir('complete'):
    
    # _move_all_subfolder_files_to_main_folder(Path(f"complete"), Path('extracted'))
    recursive_copy('complete', 'extracted', logfile)

  cleanup('complete', logfile)
  cleanup('downloading', logfile)

  logfile.write(f"Extraction complete!\n")
  logfile.write(f"=====================================================================\n\n")
  logfile.close()

main()
