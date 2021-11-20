import dlib
import numpy as np
import cv2
import time
import os
import math
import pymysql
path_screenshots = "data/screenshots/"

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor('data/dlib/shape_predictor_68_face_landmarks.dat')
conn = pymysql.connect(host="127.0.0.1", user="root", password='123456', db="mysql")
cursor = conn.cursor()
ss = os.listdir("data/image/")
for image in ss:
    cap = cv2.imread("data/image/" + image, cv2.IMREAD_UNCHANGED)
im_rd = cap
def azimuthAngle( x1,  y1,  x2,  y2):
    angle = 0.0
    dx = x2 - x1
    dy = y2 - y1
    if  x2 == x1:
        angle = math.pi / 2.0
        if  y2 == y1 :
            angle = 0.0
        elif y2 < y1 :
            angle = 3.0 * math.pi / 2.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dx / dy)
    elif x2 > x1 and  y2 < y1 :
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif x2 < x1 and y2 < y1 :
        angle = math.pi + math.atan(dx / dy)
    elif x2 < x1 and y2 > y1 :
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    return round((angle * 180 / math.pi),3)

def score(Z):
    '''
    计算正态分布的累积分布函数(Cumulative Distribution Function，CDF)
    '''
    X=-1*(Z-90)/100
    T=1/(1+.2316419*abs(X))
    D=0.3989423*math.exp(-X*X/2)
    Prob=D*T*(0.3193815+T*(-0.3565638+T*(1.781478+T*(-1.821256+T*1.330274))))
    return Prob


k = cv2.waitKey(1)
img_gray = cv2.cvtColor(im_rd, cv2.COLOR_RGB2GRAY)
faces = detector(img_gray, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
if len(faces) != 0:
    for i in range(len(faces)):

        landmarks = np.matrix([[p.x, p.y] for p in predictor(im_rd, faces[i]).parts()])
        for idx, point in enumerate(landmarks):
            if idx ==48 or idx ==49 or idx ==50 or idx==51 or idx==52 or idx==53 or idx==54 or idx==55 or idx==56 or idx==57 or idx==58 or idx==59 or idx==60 or idx==61 or idx==62 or idx==63 or idx==64 or idx==65 or idx==66 or idx==67 or idx==68:
                pos = (point[0, 0], point[0, 1])
                cv2.circle(im_rd, pos, 2, color=(255, 255, 255))
                    # cv2.putText(im_rd, str(idx + 1), pos, font, 0.2, (187, 255, 255), 1, cv2.LINE_AA)
                if idx!=48:
                    if idx!=60:
                        cv2.line(im_rd, pos1, pos, (0, 255, 0), thickness=3, lineType=8)
                if idx==48:
                    pos2=(point[0, 0], point[0, 1])
                if idx==59:
                    cv2.line(im_rd, pos, pos2, (0, 255, 0), thickness=3, lineType=8)
                if idx==60:
                    pos3 = (point[0, 0], point[0, 1])
                if idx==67:
                    cv2.line(im_rd, pos, pos3, (0, 255, 0), thickness=3, lineType=8)
                pos1 = (point[0, 0], point[0, 1])
            if idx ==36 or idx ==37 or idx ==38 or idx==39 or idx==40 or idx==41:
                pos = (point[0, 0], point[0, 1])
                cv2.circle(im_rd, pos, 2, color=(255, 255, 255))
                    # cv2.putText(im_rd, str(idx + 1), pos, font, 0.2, (187, 255, 255), 1, cv2.LINE_AA)
                if idx!=36:
                    cv2.line(im_rd, pos1, pos, (0, 255, 0), thickness=3, lineType=8)
                if idx==36:
                    pos2=(point[0, 0], point[0, 1])
                if idx==41:
                    cv2.line(im_rd, pos, pos2, (0, 255, 0), thickness=3, lineType=8)
                pos1 = (point[0, 0], point[0, 1])
            if idx ==42 or idx ==43 or idx ==44 or idx==46 or idx==45 or idx==47:
                pos = (point[0, 0], point[0, 1])
                cv2.circle(im_rd, pos, 2, color=(255, 255, 255))
                    # cv2.putText(im_rd, str(idx + 1), pos, font, 0.2, (187, 255, 255), 1, cv2.LINE_AA)
                if idx!=42:
                    cv2.line(im_rd, pos1, pos, (0, 255, 0), thickness=3, lineType=8)
                if idx==42:
                    pos2=(point[0, 0], point[0, 1])
                if idx==47:
                    cv2.line(im_rd, pos, pos2, (0, 255, 0), thickness=3, lineType=8)
                pos1 = (point[0, 0], point[0, 1])
            if idx ==17 or idx ==18 or idx ==19 or idx==20 or idx==21:
                pos = (point[0, 0], point[0, 1])
                cv2.circle(im_rd, pos, 2, color=(255, 255, 255))
                    # cv2.putText(im_rd, str(idx + 1), pos, font, 0.2, (187, 255, 255), 1, cv2.LINE_AA)
                if idx!=17:
                    cv2.line(im_rd, pos1, pos, (0, 255, 0), thickness=3, lineType=8)
                if idx==17:
                    pos2=(point[0, 0], point[0, 1])
                if idx==18:
                    cv2.line(im_rd, pos, pos2, (0, 255, 0), thickness=3, lineType=8)
                pos1 = (point[0, 0], point[0, 1])
            if idx ==22 or idx ==23 or idx ==24 or idx==25 or idx==26:
                pos = (point[0, 0], point[0, 1])
                cv2.circle(im_rd, pos, 2, color=(255, 255, 255))
                    # cv2.putText(im_rd, str(idx + 1), pos, font, 0.2, (187, 255, 255), 1, cv2.LINE_AA)
                if idx!=22:
                    cv2.line(im_rd, pos1, pos, (0, 255, 0), thickness=3, lineType=8)
                if idx==22:
                    pos2=(point[0, 0], point[0, 1])
                if idx==21:
                    cv2.line(im_rd, pos, pos2, (0, 255, 0), thickness=3, lineType=8)
                pos1 = (point[0, 0], point[0, 1])
        mouthangle1=score(abs(azimuthAngle(landmarks[57,0],  landmarks[57,1],  landmarks[42,0],  landmarks[42,1])))
        brownangle1 = score(abs(azimuthAngle(landmarks[17, 0], landmarks[17, 1], landmarks[19, 0], landmarks[19, 1])))
        s=0.7*mouthangle1*200+0.3*brownangle1*200
        sql = "insert into smile (id,score) VALUES (" + "null,'" +str(s) +"' )"
        print(sql)
        cursor.execute(sql)
        conn.commit()
    cv2.putText(im_rd, "Faces:"  + str(len(faces)), (20, 50), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    print("Faces:1;score:"+s)
else:
    print("No face detected")
# cv2.imwrite(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".jpg",im_rd, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
cv2.destroyAllWindows()
cursor.close()
conn.close()