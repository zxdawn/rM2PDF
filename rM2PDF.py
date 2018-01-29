# rM2PDF script for the reMarkable reader
# Version: 1.0
# Author: Xin Zhang

#--------------------------------------------------#
# set input_dir and output_dir as same as rMsync.sh
input_dir = '/mnt/d/rM/original_pdf/'
output_dir = '/mnt/d/rM/noted_pdf/'
t = '/mnt/d/rM/temporary/'
#--------------------------------------------------#

import numpy as np
import os,fnmatch

# get names of note_lines
note_line = []
for file in os.listdir(input_dir):
    if fnmatch.fnmatch(file,'*.lines'):
        note_line = np.append(note_line,file)

# get prefix
prefix =  [x[:-6] for x in note_line]

for id,prefix in enumerate (prefix):
    # get visible name in metdata
    pdf_data  = open(input_dir+prefix+'.metadata')
    visiable_name = pdf_data.readlines()
    visiable_name = visiable_name[10].split(":",1)[1][2:-2].replace(" ", "_")

    # convert .lines to .svg
    script =  'python '+'./rM2svg.py -i {line} -o {svg_prefix}'
    script = script.format (line=input_dir+note_line[id],svg_prefix=t+'temporary')
    os.system(script)
    # convert .svg to pdf
    os.system('svg2pdf -o '+t+'"%(base)s.pdf" '+t+'*.svg')
    os.system('rm '+t+'*.svg')

    # check notebook or document
    if os.path.isfile(input_dir+prefix+'.pdf'): # document

        # combine notes to one pdf
        os.system('convert '+t+'temporary*.pdf '+t+'note.pdf')
        # check width and height of original pdf
        width_column = "'NR==3{print $4}'"
        height_column = "'NR==3{print $5}'"
        width = os.popen('./cpdf -page-info '+input_dir+prefix+'.pdf'+' | awk {}'\
            .format(width_column)).read()
        height = os.popen('./cpdf -page-info '+input_dir+prefix+'.pdf'+' | awk {}'\
            .format(height_column)).read()

        # check landscape or portrait
        if width > height: # landscape
            size = "'"+height+' '+width+"'"
            scalerotate = './cpdf -scale-to-fit {} '.format(size)+t+'note.pdf '+\
            'AND -rotate 90 AND -upright '+t+'note.pdf '+'-o '+t+'note.pdf'
            os.system(scalerotate)
        else: # portrait
            size = "'"+width+' '+height+"'"
            scale = './cpdf -scale-to-fit {} '.format(size)+t+'note.pdf '+'-o '+t+'note.pdf'           
            os.system(scale)

        # combine note and original pdf
        os.system('./cpdf -combine-pages '+t+'note.pdf '+ input_dir+prefix+'.pdf '\
            +'-o '+output_dir+visiable_name+'.pdf')
        os.system('rm '+t+'temporary*.pdf '+t+'note.pdf')

    else: # notebook
        os.system('convert '+t+'temporary*.pdf '+output_dir+visiable_name+'.pdf')
        os.system('rm '+t+'temporary*.pdf')