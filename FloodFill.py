# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
#
# plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.


class FloodFill(object):
    def flood_fill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        if image[sr][sc] == color:
            return image

        num_rows = len(image)
        num_cols = len(image[0])

        r_cord_up = sr - 1
        r_cord_down = sr + 1
        c_cord_up = sc - 1
        c_cord_down = sc + 1

        if 0 <= r_cord_up <= num_rows:
            if image[sr][sc] == image[r_cord_up][sc]:
                for c in range(num_rows):
                    image[r_cord_up][c] = color

        if r_cord_down <= num_rows:
            if image[sr][sc] == image[r_cord_down][sc]:
                for c in range(num_rows):
                    image[r_cord_down][c] = color

        if 0 <= c_cord_up <= num_cols:
            if image[sr][sc] == image[sr][c_cord_up]:
                for c in range(num_cols):
                    image[c][c_cord_up] = color

        if c_cord_down <= num_cols:
            if image[sr][sc] == image[sr][c_cord_down]:
                for c in range(num_cols):
                    image[c][c_cord_down] = color

        image[sr][sc] = color

        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
print(f"Old image: {image}")
new_image1 = FloodFill().flood_fill(image, sr, sc, color)
print(f"New image: {new_image1}")

print()

image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
print(f"Old image: {image}")
new_image2 = FloodFill().flood_fill(image, sr, sc, color)
print(f"New image: {new_image2}")
