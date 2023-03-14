import os
from pathlib import Path
from PIL import Image
import csv

dataset_dir=["VisDrone2019-DET-train","VisDrone2019-DET-val","VisDrone2019-DET-test-dev"]
wd = os.getcwd()

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2] / 2) * dw
    y = (box[1] + box[3] / 2) * dh
    w = box[2] * dw
    h = box[3] * dh
    return (x, y, w, h)

for datadir in dataset_dir:
    lbls=os.path.join(wd,datadir,'labels')
    if not os.path.exists(lbls):
        os.makedirs(lbls)
    
    train_file = os.path.join(wd,datadir,'images.txt')
    train_file_txt = ''
        
    anns = os.listdir(os.path.join(wd,datadir,'annotations'))
    for ann in anns:
        ans = ''
        outpath = wd +'/'+datadir+'/'+ '/labels/' + ann
        if ann[-3:] != 'txt':
            continue
        with Image.open(wd +'/'+datadir+'/'+ '/images/' + ann[:-3] + 'jpg') as Img:
            img_size = Img.size
        with open(wd + '/'+datadir+'/'+'/annotations/' + ann, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if row[4] == '0':
                    continue
                bb = convert(img_size, tuple(map(int, row[:4])))
                ans = ans + str(int(row[5])-1) + ' ' + ' '.join(str(a) for a in bb) + '\n'
                with open(outpath, 'w') as outfile:
                    outfile.write(ans)
        train_file_txt = train_file_txt + wd + '/'+datadir+'/'+'/images/' + ann[:-3] + 'jpg\n'

    with open(train_file, 'w') as outfile:
        outfile.write(train_file_txt)

