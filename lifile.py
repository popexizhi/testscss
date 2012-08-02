# -*- coding: cp936 -*-
"""
加载数据文件
"""
#filename:scss\file.py
#import file

class setfiledata:
        '''file input '''
        
        def __init__(self,filename):
                self.filename = filename
                self.li_name = []
                self.all_courses = []
	#检查filename的文件是否存在，如果不存在提示用户，注销此对象


        def add_date(self):
                f = open(self.filename,"r")
                print self.filename
                #print f
                i=0
                while True:
                        line = f.readline()
                        #print line
                        if len(line) ==0:
                                break
                        li_con = line.split() # 分割每列的数据
                        
                        
                        li_dany = li_con[3].split(',')#分割课程单元
                        for j in li_dany:
                                li_date = li_con[0] +"\t"+li_con[1]+"\t"+li_con[2]+"\t"+ j
                                print li_date
                        'self.add_notedate(li_con)'
                        i = i+1
                f.close()

        def add_li_name(self,str): #增加列名称
                i = 0
                for t in str:
                        #print i
                        self.li_name.append(t)
                        i=i+1
                # print "li_con num:%d" % i
                

        def add_notedate(self,li_con):  #增加节点数据,后期修改建议标签从文件中读取
                course={}
                i=0
                # print li_con[i]
                for lname in self.li_name:
                        course[lname] = li_con[i]
                        i = i+1
                        # print i,course

                self.all_courses.append(course)
                # print "ok"

        def pr(self):
                print self.all_courses


if __name__ =="__main__":
        filenames = ["cg.txt"]
        file = []
        i = 0
        course = setfiledata(filenames[0])
        'classroom = setfiledata(filenames[1])'
        'classroom.add_date()'
        course.add_date()
        
        'course.pr()'
        
