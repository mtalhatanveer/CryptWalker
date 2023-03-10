from PIL import Image
import numpy as np

class GVC:
    def __init__(self):
        print('')

    def viscrypt(self, path):
        # Step1  Convert to Gray scale
        img = Image.open(path)
        width, height = img.size
        if width > height:
            min_size = height, height
        else:
            min_size = width, width

        newimg = img.resize(min_size)
        graysc = newimg.convert('1')
        # print(graysc)
        # graysc.show()

        # Step2 Convert Byte Image to share1 and share2
        graynp = np.array(graysc)
        # print(graynp)

        share1 = Image.new("1", min_size, "black")
        share1x = np.array(share1)
        share2 = Image.new("1", min_size, "white")
        share2x = np.array(share2)

        for i in range(len(graynp)):
            for j in range(len(graynp[i])):
                if not graynp[i][j]:
                    share1x[i][j] = True

        for i in range(len(graynp)):
            for j in range(len(graynp[i])):
                if not graynp[i][j]:
                    share2x[i][j] = False

        newimg1 = Image.fromarray(share1x)
        # newimg1.show()
        newimg2 = Image.fromarray(share2x)
        # newimg2.show()

        newimg1.save('share1.png')
        newimg2.save('share2.png')

    def videcrypt(self, f1, f2):
        s1 = Image.open(f1)
        s2 = Image.open(f2)
        width, height = s1.size
        if width > height:
            min_size = height, height
        else:
            min_size = width, width

        share1x = np.array(s1)
        share2x = np.array(s2)

        share3 = Image.new("1", min_size, "white")
        share3x = np.array(share3)
        # for i in range(len(share1x)):
        #     for j in range(len(share1x[i])):
        #         if share1x[i][j]:
        #             share3x[i][j] = True

        for i in range(len(share1x)):
            for j in range(len(share1x[i])):
                if not share2x[i][j]:
                    share3x[i][j] = False

        newimg3 = Image.fromarray(share3x)
        newimg3.save('gvdecrypted.png')
