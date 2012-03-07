
import gdata.apps

#Example how to authorize you application service
from Connector import Connector
multidomainObj = gdata.apps.service.AppsService()
Connector.connectByOauth(multidomainObj)
print multidomainObj.RetrieveAllUsers()


#Example how to create OAuth token
from OAuth import OAuth
from OAuth import POSSIBLE_SCOPES
OAuth(domain="gridcommons.com", 
                         clientKey="your client key", 
                         clientSecret="your client secret", 
                         scopes=POSSIBLE_SCOPES, 
                         appName="application name").getAccessToken()
