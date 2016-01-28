from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

MY_SQL_PASSWD = "password1"
conn = pymysql.connect(host="127.0.0.1", user='root', passwd=MY_SQL_PASSWD, db='mysql') 

cur = conn.cursor()
cur.execute("USE wikipedia") 

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message 

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()] 

def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links: 
        return dict(zip(links, [{}]*len(links)))
    return {} 

# The link tree may either be empty or contain multiple links 
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0: 
        #stop recursion and return 
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            # no links found. Cannot continue at this node 
            return {} 
    if targetPageId in linkTree.keys():
        print("TARGET "+str(targetPageId)+" FOUND!")
        raise SolutionFound("PAGE: "+str(currentPageId))

    for branchKey, branchValue in linkTree.items(): 
        try: 
            # Recurse here to continue building the tree 
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1) 

        except SolutionFound as e: 
            print(e.message) 
            raise SolutionFound("PAGE: "+str(currentPageId))
    return linkTree

try: 
    searchDepth(3876, 1, {}, 4)
    print("No Solution Found") 
except SolutionFound as e: 
    print(e.message) 