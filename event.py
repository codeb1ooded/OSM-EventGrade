#GET: Search
import requests
import json
import sys
#import requests.packages.urllib3

count =0
access_token = 'EAAM39GiUIEwBAGZA88ZBSbamEy4WcxrjWMdEek2sl98WekVicuR2gULXVfRh9LYNhGfGW1aaP600ce4Xr6XmymDm5B2h3mttqqcuX09DvSliKeKrZCznOg2Ud9Jx6AVtkFZBwaMrHLQ2EmiCMSZCMTUWpojTaLjwZD'

def search(base_url):
	results = requests.get(base_url)

        request_text = results.text
	results_json = json.loads(request_text)
	for item in results_json['data']:
		print item['name']
		print item['id']
                #print item['description']
		print ''
		global count
		count = count+1
	try:
		paging_object = results_json['paging']
		next_base_url = paging_object['next']
		search(next_base_url)
	except:
		print ''
	else:
		print ''

def main(key):
 event_keyword=key
 base_url = 'https://graph.facebook.com/v2.6/search?q='+event_keyword+'&type=event&access_token='+access_token
 #print base_url
 #print event_keyword
 search(base_url)
 print count
 #sys.exit()

