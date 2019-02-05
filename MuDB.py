import pickle
class Composer:
    def __init__(self,name):
        self.name=name
        self.album=[]
    def setalbum(self):
        print(self.name,'Selected')
        album=input('Album Name: ').title()
        if album not in self.album:
            self.album.append(album)
            print(album,'added to Composer',self.name)
        else:
            print('Album already exists.')
    def getalbum(self):
        self.album.sort()
        print(self.name,':')
        self.albumLister()
        print()
    def deleteAlbum(self):
        print(self.name,'selected')
        self.albumLister()
        albumID=int(input('Delete Album: '))
        print(self.album[albumID],'deleted')
        del self.album[albumID]
    def albumLister(self):
        for index,album in enumerate(self.album):
            print('\t\t\t{0:2d}. {1}'.format(index,album))


filename='mudb.txt'
l=[]
def readfile():
    global l
    try:
        with open(filename,'rb') as f:l=pickle.load(f)
    except:
        writefile(l)

def writefile(l):
    with open(filename,'wb') as mudb:
        pickle.dump(l,mudb)


def deleteComposer(comp):
        print(comp.name,'deleted')
        l.remove(comp)
def selectComposer():
    return l[int(input('Select Composer: '))]

def listAppend(composer):
    l.append(Composer(composer))
    print('Composer {0} added'.format(composer))

def composerLister():
    for index,cname in enumerate(l):
                    print('\t\t\t{0:2d}. {1}'.format(index,cname.name))

if __name__=='__main__':
    print('++++++______Music DataBase______++++++')
    readfile()
    while True:
        try:
            mode=int(input('\n1.ADD COMPOSER\n2.ADD ALBUM\n3.SHOW DATABASE\n\
4.DELETE COMPOSER\n5.DELETE ALBUM\n6.SAVE\n7.RESTART\n0.EXIT\nENTER YOUR CHOICE: '))
            if 8>mode>=0:
                if mode==0:break
                elif mode==1:
                    composer=input('Composer Name: ').title()
                    try:
                        for c in l:
                            if composer == c.name:
                                print('Composer {0} Already Exists'.format(composer))
                                break
                        else:listAppend(composer)
                    except:listAppend(composer)

                elif mode==6:
                    if input('Do you want to save? y/n\n')=='y':
                        writefile(l)
                        print('Saved to DataBase.')
                    else:print('not saved')
                elif mode==7:
                    readfile()
                    print('changes undone.')

                else:
                    composerLister()
                    c=selectComposer()
                if mode==2:c.setalbum()
                elif mode==3:c.getalbum()
                elif mode==4:deleteComposer(c)
                elif mode==5:c.deleteAlbum()
            else:print ("Incorrect Choice.Try Again")
            
        except Exception as err:
            print(err)
            continue
    input("\t\t\t\tTHANK YOU")




    
