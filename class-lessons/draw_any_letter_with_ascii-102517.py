pixelSize = 36
gridSize = 50

letter_a = """
-------
--xxx--
-----x-
--xxxx-
-x---x-
-x--xx-
--xx-x-
-------
"""
letter_e = """
-------
--xxx--
-x---x-
-x---x-
-xxxxx-
-x-----
--xxxx-
-------
"""



x = 100

def drawShape(shape):
    y = 800
    for row in shape.splitlines():
        x = 100
        counter = 1
        for pix in row: 
            if pix == "x":
                # print "yes pixel"
                print counter
                fill(0,0,0+.25*counter)
                rect(x,y, pixelSize,pixelSize)
                counter = counter + 1
            else:
                # print "no pixel"
                fill(1,1,.5)
                fill(1-.075*counter,1-.1*counter,1-.075*counter)
                oval(x,y, pixelSize,pixelSize)
                counter = counter + 1
            x = x + gridSize
        y = y - gridSize   
        
drawShape(letter_a)
translate(7*gridSize)
drawShape(letter_e)