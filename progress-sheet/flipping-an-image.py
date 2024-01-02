class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i].reverse()
            j = 0
            for j in range(len(image)):
                    image[i][j] = 1-image[i][j]
               
        return image
        