import requests
import json

import mwparserfromhell as mwph
def pretty(jdata):    

    str = json.dumps(jdata, sort_keys=True, indent=4).decode('string_escape')    

    return str

def saveas(sdata, fname):    

    f = open(fname,'w')    

    f.write(sdata)

    f.close() 

title='parsing'
pretty_text = "pretty_text"
response = requests.get("http://en.wikipedia.org/w/api.php?format=json&action=query&titles="+str(title)+"&prop=revisions&rvprop=content")
print response 
jsondata = response.json()

#print jsondata
print jsondata.keys() #[u'batchcomplete', u'query']
#print jsondata['query']
print type(jsondata['query'])

content =  jsondata['query']['pages'].values()[0]['revisions'][0].values()[0]
print content
wikicode = mwph.parse(content)


print "filter comments:",wikicode.filter_comments()

print "filter headings",wikicode.filter_headings()

print "filter wikilinks",wikicode.filter_wikilinks() 

text = wikicode.strip_code()
saveas(pretty(text), '/home/sudeepgaddam/data_science/labs/lab2/'+pretty_text+'.txt') 
#print "text",text 
#print jsondata['query']['pages'].values()[0] 

#fp=open('/home/sudeepgaddam/data_science/labs/lab2/parsing.json','r')

#jsondata=json.load(fp);

#fp.close()
#saveas(pretty(jsondata), '/home/sudeepgaddam/data_science/labs/lab2/'+title+'.json') 
