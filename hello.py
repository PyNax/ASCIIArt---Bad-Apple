import time,os,cv2,winsound
CHARS = '  .,-~:;=!*#$@'
CHARLEN = len(CHARS)
nw = 100
start = 0
fps_60 = 1 / 60
this_spf_24,frame,makedelay = 0,0,0
cap = cv2.VideoCapture('BadApple24fps.mp4')

""" winsound.PlaySound('BadApple.wav',winsound.SND_ASYNC) """
timer = time.time()
print('\x1b', end='')
while cap.isOpened():
    os.system('cls')
    nowtime = time.time()
    fpc = nowtime - start
    overfps = fps_60 > fpc
    overfpstimes = 0
    realtime = nowtime - timer
    ret, img = cap.read()
    print("frame per command :", fpc, end='   ')
    print('waittime :', fps_60 - fpc, end='   ')
    print('overfps :',overfpstimes, end='   ')
    print('frame :', frame, end='   ')
    print('realtime :', realtime, end='   ')
    print('fps :', int(1 / fpc))
    if not ret:
        break
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h, w = img.shape
    nh = int(h / w * nw /2)

    img = cv2.resize(img, (nw,nh))

    for row in img:
        for pixel in row:
            index = int(pixel / 255 * (CHARLEN - 1))
            if index > (CHARLEN - 1):
                print(' ',end='')
            else:
                print(CHARS[index],end='')
        
        print() 
    start = time.time()
    if overfps:
        overfpstimes = overfpstimes + 1
    if (fps_60 - fpc > 0):
        time.sleep(fps_60 - fpc)
    frame = frame + 1
    if (frame/24).is_integer():
        this_spf_24 = this_spf_24 + 1
            