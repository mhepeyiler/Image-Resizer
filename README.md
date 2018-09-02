# Image-Resizer

It is quite simple terminal image resizer. It can be resize the images using four different algorithm. These are;

- Neighbour
- Bilinear
- Bicubic
- Lanczos

Default image interpolation algorithm is bicubic.

## Example of usage ##

```
c:\python resizer.py -f image.jpg -o output.jpg -r 4 -a lanczos
```


-f/--file for input image file
-o/--output for output image file name.
-r/-ratio to specify the resize ratio. R>1 the image will be bigger, otherwise the image will be smaller. 
-a/--algorithm to specify the interpolation algorithm, which is explained above.
