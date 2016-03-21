#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from articles.models import News
import random



# Create your views here.


def articles(request):
    model = News.objects.all() # getting News objects list
   # modelSerialize =  serializers.serialize('json', News.objects.all())
    random_generator = random.randint(1,News.objects.count())    
    context = {'models':model, 
	          'title' : 'Articles' , 
			  'num_of_objects' : News.objects.count() , 
			  'random_order' :  random.randint(1,random_generator) ,
			  'random_object' : News.objects.get(id = random_generator ) ,
			  'first4rec' : model[0:4],
    		  'next4rec' : model[4:],

    		  #'data' : serializers.serialize("json", News.objects.all()),
              
			  }

    
    News.objects.filter(id = 2).update(likecount = 1)
    
	#serialized_obj = serializers.serialize('json', [ obj, ])
    return render(request, 'articles.html',context)

def listOfArticles(request,article_id):   
    return render(request, 'articlesDetail.html',{'listing': News.objects.get(id=article_id) , 'title' : 'Articles Detail' , 'first4rec' :News.objects.all()[0:4],})


def getVoteCount(request):
    
	context = { }
	print request.GET.get('count')
	return render(request, 'articles.html',context)