def f(z, c):
    return [z[0]**2 - z[1]**2 + c[0], 2 * z[0] * z[1] + c[1]]


def mandelbroot(c):
    global no_of_iter
    
    curr_iter = f([0, 0], c)
    
    for i in range(no_of_iter - 1):
        curr_iter = f(curr_iter, c)

    return abs(curr_iter[0]) > 2 or abs(curr_iter[1]) > 2
    

iter_real_no = 25
no_of_iter = 1

def setup():
    global no_of_iter
    
    fullScreen()
    background(255)
    loadPixels()
    print(width, height)
    # 1366 768 384
    
    for n in range(iter_real_no):
        for i in range(width):
            for j in range(height):
                mb = mandelbroot([map(i, 0, width - 1, -2.55729167, 1), map(j, 0, height - 1, -1, 1)])
                if not mb:
                    pixels[width * j + i] = color(255 * (no_of_iter % iter_real_no) / iter_real_no)
        print('{}%'.format(floor(100 * no_of_iter / iter_real_no)))
        no_of_iter += 1
        
    updatePixels()
    
