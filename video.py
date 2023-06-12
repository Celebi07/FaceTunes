import cv2
import math

def video_detection_vid(path_x):
    video_capture = path_x
    #Create a Webcam Object
    cap=cv2.VideoCapture(video_capture)
    frame_width=int(cap.get(3))
    frame_height=int(cap.get(4))

    # model=YOLO('ModelWeights\\best.pt')
    # classNames = ["GUN","Grenade","Gun","Knife","Not Knife","Pistol"]
    while True:
        success, img = cap.read()
        # results=model(img,stream=True,conf=0.5)
        for r in results:
            boxes=r.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
                print(x1,y1,x2,y2)
                conf=math.ceil((box.conf[0]*100))/100
                cls=int(box.cls[0])
                class_name=classNames[cls]
                label=f'{class_name} {conf*100}%'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                print(t_size)
                c2 = x1 + t_size[0], y1 - t_size[1] - 3

                color = (105, 245,66)
                if (conf >=0.75):
                    color = (66, 138, 245)
                if (conf >= 0.9):
                    color = (66, 66, 245)
                
                cv2.rectangle(img, (x1,y1), (x2,y2), color ,3)
                cv2.rectangle(img, (x1,y1), c2, color, -1, cv2.LINE_AA)  # filled
                cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=2,lineType=cv2.LINE_AA)

                # print(img)
                # if(conf>=0.85):
                #     start = timer()
                #     with concurrent.futures.ThreadPoolExecutor() as executor:
                #         future = executor.submit(em,"dasyagupta@gmail.com",img)
                #         result = future.result()
                    # em("dasyagupta@gmail.com",img)
                    # end=timer()
                    # print(end-start)
                
        yield img
        #out.write(img)
        #cv2.imshow("image", img)
        #if cv2.waitKey(1) & 0xFF==ord('1'):
            #break
    #out.release()
cv2.destroyAllWindows()