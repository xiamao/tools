#coding = utf-8

import pickle
from gearman import GearmanClient  

params = [4, 'http://md5.gromweb.com/', '7815696ecbf1c96e6894b779456d330e']
picp = pickle.dumps(params)

new_client = GearmanClient()  
current_request = new_client.submit_job('borg', picp)  
new_result = current_request.resul
#t_result = pickle.loads(new_result)  
print new_result