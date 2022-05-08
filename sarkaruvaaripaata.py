# import required module
!pip install requests
!pip install json
!pip install urllib3
!pip install yagmail
import requests
import json
import time
# mention url
url = "https://www.fast2sms.com/dev/bulk"


# create a dictionary
my_data = {
	# Your default Sender ID
	'sender_id': 'FastSM',
	
	# Put your message here!
	'message': 'Sarkaru vaari paata tickets release ayyayi chudu.',
	
	'language': 'english',
	'route': 'p',
	
	# You can send sms to multiple numbers
	# separated by comma.
	'numbers': '8309734591,9491644788,9182082976,9533798579'	
}

# create a dictionary
headers = {
	'authorization': 'KhEoPsget2bRI8WwZnTXz37iUpNdJc0mkGQSvy4F6frLHlVOAxZ2dBNQgwv0ekuyalpKtHLcrIJxqGX8',
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache"
}

from bs4 import BeautifulSoup
import time
import yagmail
import urllib3
import urllib.request as urllib3


while(1):
  book_my_show_url = "https://in.bookmyshow.com/buytickets/sarkaru-vaari-paata-vijayawada/movie-vija-ET00131962-MT/20220513"
  requester = urllib3.Request(book_my_show_url, headers={'User-Agent': "Magic Browser"})
  connector = urllib3.urlopen(requester)
  connector_reader = connector.read()
  soup = BeautifulSoup(connector_reader, "lxml")
  text = soup.get_text()
  if "20220513" in text:
    response = requests.request("POST",url,data = my_data,headers = headers)
    returned_msg = json.loads(response.text)
    break
  time.sleep(60)
print(returned_msg['message'])
