# You are given 2 out of 3 of the angles in a triangle, in degrees.
# The sum of angles of any triangle is always 180 degrees.
# Write a function that classifies the missing angle as either "acute", "right",
# or "obtuse" based on its degrees:
    # An acute angle is one smaller than 90 degrees.
    # A right angle is one that is exactly 90 degrees.
    # An obtuse angle is one greater than 90 degrees (but smaller than 180 degrees).

# For example: missing_angle(11, 20) should return "obtuse", since the missing
# angle would be 149 degrees, which makes it obtuse.

def missing_angle(angle1, angle2):
    if angle1 + angle2 > 90:
        return "acute"
    elif angle1 + angle2 == 90:
        return "right"
    else:
        return "obtuse"

print(missing_angle(27, 59)) #➞ "obtuse"
print(missing_angle(135, 11)) #➞ "acute"
print(missing_angle(45, 45)) #➞ "right"
