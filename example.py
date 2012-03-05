from OAuth import OAuth
from OAuth import POSSIBLE_SCOPES
final_access_key = OAuth(domain="gridcommons.com", 
                         clientKey="226704969048.apps.googleusercontent.com", 
                         clientSecret="b5l6pRTLL-aZWbKyOq4KyuxE", 
                         scopes=POSSIBLE_SCOPES[0:3] + POSSIBLE_SCOPES[6:9], 
                         appName="Some App Name").getAccessToken()
print final_access_key