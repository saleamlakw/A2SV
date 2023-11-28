class Solution(object):
    def flipAndInvertImage(self, image):
        for im in range(len(image)):
            l,r=0,len(image[im])-1
            while l<=r:
                if l==r:
                    if image[im][l]:
                        image[im][l]=0
                    else:
                        image[im][l]=1
                else:
                    image[im][l],image[im][r]=image[im][r],image[im][l]
                    if image[im][l]:
                        image[im][l]=0
                    else:
                        image[im][l]=1
                    if image[im][r]:
                        image[im][r]=0
                    else:
                        image[im][r]=1
                l+=1
                r-=1
        return image
        