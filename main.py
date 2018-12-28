#加载图片并且绘制圆形和直线
'''
#circle(img,center,radius,color,thickness,lineType,shift)
#img:要画的圆所在的图像
#center:圆心坐标，如(100，100)
#radius：半径，如10
#color：圆边框颜色，如（0，0,255）,BGR
#thickness：正值表示圆边框宽度，负值表示填充圆形
#lineType：圆边框线型，为0,4,8
#shift：圆心坐标和半径的小数点位数

#line(img,pt1,pt2,color,thickness,linetype,shift)
img:要画的直线所在的图像
pt1:直线起点
pt2:直线终点
color:线条颜色，如（0,0,255）红色，BGR
thickness:线条宽度
lineType：4,8，CV_AA（抗锯齿）
shift:坐标点小数点位数

#rectangle(img,pt1,pt2,color,thickness,lineType,shift)
img:要画的矩形所在的图像
pt1：矩形的左上角坐标
pt2：矩形的右下角坐标
color：线条颜色
thickness：线条宽度
lineType：
shfit：坐标点小数点位数

#ellipse(img,center,axes,rotateAngle,startAngle,endAngle,color,thickness,lineType,shift)
img:要画的椭圆所在的图像
center：椭圆的中心点
axes：椭圆的x半轴和y半轴的大小
rotateAngle：椭圆的旋转角度
startAngle：椭圆的起始角度
endAngle：椭圆的终止角度

#putText(img,text,point,fontFace,fontscale,color,thickness,lineType,bottomLeftorigh)
img:显示文字的图像
text:待显示的字体
point:文字在图像中的左下角坐标
fontFace:字体类型
fontscale:字体大小
color:文本颜色
bottomLeftOrigin:true图像数据原点在左下角，false图像数据原点在左上角
'''

import cv2 as cv

img = cv.imread("c:\\quanwei\\BMP\\123.bmp")

#text
text="Hello World"
text_point=(100,100)
fontFace=cv.FONT_HERSHEY_SIMPLEX
font_scale=2

#circle
point_size = 1
point_color = (0,0,255)
thickness = 4
point_list = [(160,160),(136,160),(150,200),(200,180),(120,150),(145,180)]

#line
pt1 = (10,10)
pt2 = (100,100)

#ellieps
center=(200,200)
axes=(100,50)
roateangle=0
startAngle=0
endAngle=360

for point in point_list:
    cv.circle(img,point,point_size,point_color,thickness)

cv.circle(img,(160,160),60,point_color,0)

cv.line(img,pt1,pt2,point_color,thickness,4)

cv.rectangle(img,pt1,pt2,point_color,thickness,4)

cv.ellipse(img,center,axes,roateangle,startAngle,endAngle,point_color,thickness,4)

cv.putText(img,text,text_point,fontFace,font_scale,point_color,thickness,4)

cv.namedWindow("image")

cv.imshow('image',img)

cv.waitKey(10000)

cv.destroyAllWindows()

