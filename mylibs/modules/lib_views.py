from django.contrib import admin
from mylibs.modules import lib_datetime



def getAssignData(request, data):
    year = lib_datetime.getYear()
    hour = lib_datetime.getHour()
    if hour <= 4 or hour >= 18:
        greeting = 'こんばんは'
    elif hour >= 10:
        greeting = 'こんにちは'
    else:
        greeting = 'おはようございます'

    assign_data = {
				'common': {
					'age': lib_datetime.getAge(lib_datetime.getDateObject(1992,8,28)),
					'hour': hour,
					'season': lib_datetime.getSeason(),
					'greeting': greeting,
				},
        'header': {
					'menu':getHeaderMenu(request)
				},
        'footer': {
					'copyright_year' : year
				},
        'content': data,
    }
    return assign_data


def getHeaderMenu(request):
    return {
        'TOP':{
            'label': 'Top',
            'urlname': 'top',
            'active': request.path == '/',
        },
        'NEWS':{
            'label': 'News',
            'urlname': 'news',
            'active': request.path.startswith('/news/'),
        },
        # 'BLOG':{
        #     'label': 'Blog',
        #     'urlname': 'blog',
        #     'active': equest.path.startswith('/blog/'),
        # },
        'CONTACT':{
            'label': 'Contact me',
            'urlname': 'inquiry',
            'active': request.path.startswith('/inquiry/'),
        }
    }