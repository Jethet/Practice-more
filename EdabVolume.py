# Create a function that gets an object arguments with height, width and length
# of a box and returns the volume of the box.
# Remember that the values are in an object.

def volume_of_box(sizes):
    w = sizes.get("width")
    l = sizes.get("length")
    h = sizes.get("height")
    return w * l * h

print(volume_of_box({ "width": 2, "length": 5, "height": 1 })) #➞ 10
print(volume_of_box({ "width": 4, "length": 2, "height": 2 })) #➞ 16
print(volume_of_box({ "width": 2, "length": 3, "height": 5 })) #➞ 30
