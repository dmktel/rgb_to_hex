'''
The rgb function is incomplete. Complete it so that passing in RGB decimal
 values will result in a hexadecimal representation being returned. 
 Valid decimal values for RGB are 0 - 255. Any values that fall out
  of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, 
the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''

# My solution
def rgb(r, g, b):
    rgb_l = [r, g, b]
    for i in range(len(rgb_l)):
        if rgb_l[i] < 0:
            rgb_l[i] = 0
        elif rgb_l[i] > 255:
            rgb_l[i] = 255
        result = ('{:02x}{:02x}{:02x}').format(rgb_l[0], rgb_l[1], rgb_l[2])
    return result.upper()

# Code wars best practice
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

