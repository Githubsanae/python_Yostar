
class Picture(object):
    def __init__(self,id,title,pageCount,type=None):
        self.id=id
        self.title=title
        self.pageCount=pageCount
        self.type=type




if __name__ == '__main__':
    test=Picture('url',123456789,'koishi',1,None)
    print(test.url)

