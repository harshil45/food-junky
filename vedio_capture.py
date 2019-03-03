import cv2
winName='live ideo feed capture'
cv2.namedWindow(winName)
cap=cv2.VideoCapture(0)
#cap.set(3,1024)
#cap.set(4,768)
print('width:'+str(cap.get(3)))
print('height:'+str(cap.get(4)))
i=0
Codec=cv2.VideoWriter_fourcc('X','V','I','D')
filename='my video.avi'
framerate=25
resolution=(640,480)
videofileoutput=cv2.VideoWriter(filename,Codec,framerate,resolution)
if cap.isOpened():
    ret,frame=cap.read()
    print(ret)
    print(frame)
else:
    ret=false
while ret:
    ret,frame=cap.read()
    videofileoutput.write(frame)
    cv2.imshow(winName,frame)
   

    ''' if cv2.waitKey(1)==13:
        cv2.imwrite('img'+str(i)+'.jpg',frame)
        i+=1
    '''
    if cv2.waitKey(1)==27:
        videofileoutput.release()
        #cv2.imwrite('img1.png',frame)
        cv2.destroyAllWindows()
        cap.release()
        break
