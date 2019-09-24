import os
import shutil
import glob
import moviepy.editor as mpy

def manage():
    path = os.getcwd()
    print(path)
    '''
    try:
        os.mkdir(path+'\\a_folder')
    except FileExistsError:
        print('file exist... should work')
    
    file_list = glob.glob('*.png')
    for file in file_list:
        #print(file)
        shutil.move(path+'\\'+file,path+'\\a_folder') # copy files into new dir
    '''
    #delete the .eps
    file_list = glob.glob('*.eps')
    for file in file_list:
        os.unlink(path+'\\'+file) #delete files
    file_list = glob.glob('*.png')
    for file in file_list:
        os.unlink(path+'\\'+file) #delete files


def main():
    file_list = glob.glob('*.png')
    gif_name = 'spin7_vid'
    for elem in file_list:
        print(elem)
    fps = 47
    #list of png's
    clip = mpy.ImageSequenceClip(file_list,fps = fps)
    clip.write_gif('{}.gif'.format(gif_name),fps=fps)

main()
manage()

