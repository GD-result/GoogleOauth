'''
Created on 06.03.2012

@author: dreambit

@organization: GridDinamycs
'''
import pickle
import gdata.apps
class Connector:
    """
    Authorize you application service
    """
    @staticmethod
    def connectByOauth(application, key_file_name="oauth.txt"):
        oauthfile = open(key_file_name, 'rb')
        domain = oauthfile.readline()[0:-1]
        application.domain = domain
        token = pickle.load(oauthfile)
        oauthfile.close()
        
        application.domain = domain
        application.SetOAuthInputParameters(gdata.auth.OAuthSignatureMethod.HMAC_SHA1, 
                                       consumer_key=token.oauth_input_params._consumer.key, 
                                       consumer_secret=token.oauth_input_params._consumer.secret)
        token.oauth_input_params = application._oauth_input_params
        application.SetOAuthToken(token)
        return application
