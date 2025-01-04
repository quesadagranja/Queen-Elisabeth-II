# Queen-Elisabeth-II

This Python script processes an input image in several steps to create a mirrored and reordered version of it.

First, the script creates a new image that is twice the width and height of the original image. It arranges the original image in the top-left corner, its horizontally mirrored version in the top-right, its vertically mirrored version in the bottom-left, and a combined horizontally and vertically mirrored version in the bottom-right.

After generating this larger mirrored image, the script divides it into vertical bands. The number of bands is determined by the width of the image and a user-defined pixel_ratio parameter. These bands are reordered such that the first band is followed by the last band, the second by the second-to-last, and so on. The reordered bands are stitched together to form a new image.

In the final step, the script further divides the vertically reordered image into horizontal bands. Again, the number of bands is calculated based on the height of the image and the pixel_ratio. These horizontal bands are reordered in the same pattern as the vertical bands. The final reordered image is saved as a separate output.

Each step ensures the modified images are saved as distinct files, maintaining a clear progression of transformations from the original image to the final output.
