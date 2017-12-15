import os
for subdir, dirs, files in os.walk('./'):
    for file in files:
      if 'STL' in file or '.stl' in file:
          command = 'ctmconv ' + file + ' ' + file[0:len(file)-4]+'.obj'
          os.system(command)
