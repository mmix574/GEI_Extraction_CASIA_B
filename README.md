# GEI_Extraction_CASIA_B

Demo:

![](https://raw.githubusercontent.com/mmix574/GEI_Extraction_CASIA_B/master/demo_image/1.png)

![](https://raw.githubusercontent.com/mmix574/GEI_Extraction_CASIA_B/master/demo_image/2.png)


这是一个用于生成步态能量图的Python程序，可以将行人剪影序列转换为单张步态特征图像。
运行环境
bashCopypip install numpy matplotlib imageio scipy scikit-image
代码功能

读取剪影图像序列
对每张图像进行处理：

计算质心
裁剪对齐
统一大小调整


生成最终的步态能量图

使用方法

准备数据：将剪影图像放在指定目录下
修改代码中的图像路径
运行程序即可得到步态能量图结果

主要函数说明

mass_center(): 计算图像质心
image_extract(): 图像预处理，包括裁剪和大小调整

注意事项

输入图像需为黑白剪影图
默认输出大小为128x64像素
