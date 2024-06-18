import copy
import math
from PyPDF2 import PdfReader, PdfWriter

def split_pages2(src, dst):
    try:
        with open(src, 'r+b') as src_f, open(dst, 'w+b') as dst_f:

            input = PdfReader(src_f)
            output = PdfWriter()

            for i in range(len(input.pages)):
                # make two copies of the input page
                pp = input.pages[i]
                p = copy.copy(pp)
                q = copy.copy(pp)
                
                # the new media boxes are the previous crop boxes
                p.mediabox = copy.copy(p.cropbox)
                q.mediabox = copy.copy(p.cropbox)
                        
                x1, x2 = p.mediabox.lower_left
                x3, x4 = p.mediabox.upper_right
                
                x1, x2 = math.floor(x1), math.floor(x2)
                x3, x4 = math.floor(x3), math.floor(x4)
                x5, x6 = x1+math.floor((x3-x1)/2), x2+math.floor((x4-x2)/2)

                if (x3-x1) > (x4-x2):
                    # horizontal
                    q.mediabox.upper_right = (x5, x4)
                    q.mediabox.lower_left= (x1, x2)

                    p.mediabox.upper_right = (x3, x4)
                    p.mediabox.lower_left = (x5, x2)
                else:
                    # vertical
                    p.mediabox.upper_right = (x3, x4)
                    p.mediabox.lower_left= (x1, x6)

                    q.mediabox.upper_right = (x3, x6)
                    q.mediabox.lower_left= (x1, x2)


                p.artbox = p.mediabox
                p.bleedbox = p.mediabox
                p.cropbox = p.mediabox

                q.artbox = q.mediabox
                q.bleedbox = q.mediabox
                q.cropbox = q.mediabox
                
                output.add_page(q)
                output.add_page(p)
                

            output.write(dst_f)
            src_f.close()
            dst_f.close()

            return 1
    except:
        print("Smthing went wrong")
        return 0
    


