
from time import time

from django.db import models




def autogenerated_Main_Image_Name(instance , filename):
    
    print 'uploadedImg/main/' + str(int(time())) 
    return 'uploadedImg/main/' + filename 
    	
def autogenerated_Sub_Image_Name(instance , filename):
    file_Extension = filename.split('.')[-1]
    return 'uploadedImg/sub/'  + filename 
    	

class News(models.Model):
    title = models.CharField("Title", max_length = 256)
    author_Detail = models.CharField("Author" , max_length = 128)
    date = models.DateTimeField("Published Date")
    m_image = models.ImageField("Main Image ", 
        upload_to =  autogenerated_Main_Image_Name ,)
    s_Image = models.ImageField("Sub Image",              #next step store m_image and s_iamge i a seperate folder
        upload_to = autogenerated_Sub_Image_Name,)
    body = models.TextField("Main Article")
    likecount = models.TextField("LikeCount" , default="0",max_length = 1000,blank=True,editable=False)
    

    class Meta:
         verbose_name_plural = "News"
         ordering = ['-date']

    def __len__():
          return len(News)
    	
    def __unicode__(self):
          return self.title