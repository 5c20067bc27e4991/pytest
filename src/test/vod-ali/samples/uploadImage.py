# -*- coding: UTF-8 -*-
from voduploadsdk.AliyunVodUtils import *
from voduploadsdk.AliyunVodUploader import AliyunVodUploader
from voduploadsdk.UploadImageRequest import UploadImageRequest 

# 测试上传本地图片
def testUploadLocalImage(accessKeyId, accessKeySecret, filePath):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadImageRequest = UploadImageRequest(filePath)
        uploadImageRequest.setTitle('test upload local image')  # 设置图片标题，默认为空
        imageId, imageUrl = uploader.uploadImage(uploadImageRequest, True)
        print("file: %s, imageId: %s, imageUrl: %s" % (uploadImageRequest.filePath, imageId, imageUrl))
        
    except AliyunVodException as e:
        print(e)

# 测试上传网络图片
def testUploadWebImage(accessKeyId, accessKeySecret, fileUrl):
    try:
        uploader = AliyunVodUploader(accessKeyId, accessKeySecret)
        uploadImageRequest = UploadImageRequest(fileUrl)
        uploadImageRequest.setTitle('test upload web image')  # 设置图片标题，默认为空
        imageId, imageUrl = uploader.uploadImage(uploadImageRequest, False)
        print("file: %s, imageId: %s, imageUrl: %s" % (uploadImageRequest.filePath, imageId, imageUrl))
        
    except AliyunVodException as e:
        print(e)


####  执行测试代码   ####   
accessKeyId = 'LTAIbpumCihkcYno0'
accessKeySecret = '04uI4ckSCpCb0ndTQFBhgAw60GW6VNo'

localFilePath = r'C:\Users\Guanglin\Desktop\bd_logo1.png'
testUploadLocalImage(accessKeyId, accessKeySecret, localFilePath)

fileUrl = 'http://pi.weather.com.cn/i/product/pic/l/sevp_nmc_stfc_sfer_er24_achn_l88_p9_20190303130002400.jpg'
#testUploadWebImage(accessKeyId, accessKeySecret, fileUrl)

        

