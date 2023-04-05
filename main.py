import colorgram

colors = colorgram.extract("hirst.jpg", 5)

colors_list = []

for color in colors:
    rgb = color.rgb.r, color.rgb.g, color.rgb.b
    colors_list.append(rgb)

print(colors_list)