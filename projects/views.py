from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        'id':'1',
        'title':"Ecommerce Website",
        'description':'Fully Functional ecommerce Website'
    },
    {
        'id': '2',
        'title': "Portfolio Website",
        'description': 'This was a project where I built out my portfolio website'
    },
    {
        'id': '3',
        'title': "Social Network",
        'description': 'Amazing open source project'
    },

]




def projects(request):
    page = 'Projects'
    number = 20
    context = {'Apage': page, 'Number': number, 'data': projectList}
    return render(request , 'projects/projects.html', context)


def project(request , pk):
    ProjectObj = None
    for i in projectList:
        if(i['id'] == pk):
            ProjectObj = i
    return render(request , 'projects/single-project.html' , {'ProjectObj' : ProjectObj})