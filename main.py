import colorgram

colors = colorgram.extract("hirst.jpg", 5)

colors_list = []

for i in range(len(colors)):
    rgb = colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b
    colors_list.append(rgb)

print(colors_list)