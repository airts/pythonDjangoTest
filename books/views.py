from django.http import HttpResponse



def home(request):

    D = {}
    D = {'name':'airts', 'surname':'s','year':1989}

    d = D.copy()

    d.pop('year')
    D.update({'aa':'aa'})
    del D['aa']


    content = '<div>{0} <br/> {1} <br/> {2}{3}</div'.format(D.keys(), d.values(), d.get('year','nothing'),d.__len__())
    dictionary = {'1': 'one', '2': 'two', '3': 'there'}

    for key,value in dictionary.iteritems():
        content+= '<br/><div>{0} {1}</div>'.format( key, dictionary[key])

    list = ['saa','sbb','scc']
    dd = dict((x,x) for x in list)




    return HttpResponse(content)

