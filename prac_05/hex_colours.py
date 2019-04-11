hex_colour = {"aliceBlue": "#f0f8ff", "apuamarine1": "#7fffd4", "AntiqueWhite2": "#eedfcc", "aquamarine2": "#76eec6",
              "blue1": "#0000ff", "BlueViolet": "#8a2be2", "CadetBlue2": "#8ee5ee", "chartreuse2": "#76ee00",
              "CornflowerBlue": "#6495ed", "DarkViolet": "#9400d3"}
colour = input(" enter a colour: ")
while colour != "":
    if colour in hex_colour:
        print(colour, "is", hex_colour[colour])
    else:
        print("invaid colour option ")
    colour = input(" enter a colour: ")
