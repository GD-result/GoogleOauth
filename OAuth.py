'''
Created on 04.03.2012

@author: dreambit

@organization: GridDinamycs

'''
import webbrowser
import gdata.apps.service
import pickle

POSSIBLE_SCOPES = ['https://apps-apis.google.com/a/feeds/groups/', # Groups Provisioning API
                     'https://apps-apis.google.com/a/feeds/alias/', # Nickname Provisioning API
                     'https://apps-apis.google.com/a/feeds/policies/', # Organization Provisioning API
                     'https://apps-apis.google.com/a/feeds/user/', # Users Provisioning API
                     'https://apps-apis.google.com/a/feeds/emailsettings/2.0/', # Email Settings API
                     'https://apps-apis.google.com/a/feeds/calendar/resource/', # Calendar Resource API
                     'https://apps-apis.google.com/a/feeds/compliance/audit/', # Audit API
                     'https://apps-apis.google.com/a/feeds/domain/', # Admin Settings API
                     'https://www.googleapis.com/auth/apps/reporting/audit.readonly', # Admin Audit API
                     'https://www.googleapis.com/auth/apps.groups.settings', # Group Settings API
                     'https://www.google.com/m8/feeds/profiles', # Profiles API
                     'https://www.google.com/calendar/feeds/', # Calendar Data API
                     'https://www.google.com/hosted/services/v1.0/reports/ReportingData']   # Reporting API

#REQUEST_TOKEN_URL = 'https://www.google.com/accounts/OAuthGetRequestToken'
#AUTHORIZATION_URL = 'https://www.google.com/accounts/OAuthAuthorizeToken'
#ACCESS_TOKEN_URL = 'https://www.google.com/accounts/OAuthGetAccessToken'

class OAuth:
    '''
    This class is used to authorize, and getting access key to Google's services
    '''
    def __init__(self, domain="gridcommons.com", clientKey="anonymous", clientSecret="anonymous", scopes=POSSIBLE_SCOPES, appName="Google Apps Manager"):
        '''
        @type domain: String
        @type clientKey: String
        @type clientSecret: String
        @type appName: String
        @param domain: The domain where you get the access rights
        @param clientKey: Your ClienKey
        @param clientSecret: Your ClientSecret
        @param appName: Your application name
        ''' 
        self.domain = domain
        self.clientKey = clientKey
        self.clientSecret = clientSecret
        self.appName = appName
        self.apps = gdata.apps.service.AppsService(domain=self.domain)
        self.scopes = scopes
        
        
    def getOAuthAuthorizationURL(self, scopes=POSSIBLE_SCOPES, printAuthorizationUrl=False):
        '''
        @type scopes: list
        @type printAuthorizationUrl: boolean
        @rtype: String
        @param printAuthorizationUrl: If true, output AuthorizationUrl value to the console
        @return: The link where the user will be redirected to confirm access
        '''
        #Setting parameters
        self.apps.SetOAuthInputParameters(gdata.auth.OAuthSignatureMethod.HMAC_SHA1,
                                          consumer_key=self.clientKey,
                                          consumer_secret=self.clientSecret)
        
        #Application's displayname
        self.fetchParams = {'xoauth_displayname':self.appName}
        #Getting first request token
        self.requestToken = self.apps.FetchOAuthRequestToken(scopes=scopes,
                                                             extra_parameters=self.fetchParams)
        #Application's name
        urlParams = {'hd': self.domain}
        #Generating URL to grant access
        url = self.apps.GenerateOAuthAuthorizationURL(request_token=self.requestToken,
                                                      extra_params=urlParams)
        if printAuthorizationUrl:
            print url
        return url    
    
    def getAccessToken(self):
        '''
        This method must be called for getting the final access code
        '''
        #Getting URL to grant access
        url = self.getOAuthAuthorizationURL(self.scopes, printAuthorizationUrl=True)
        print "Now script will open a web page in order for you to grant <%s> access" % self.fetchParams["xoauth_displayname"]
        #Opening URL
        webbrowser.open(url)
        raw_input("Once you have granted access, press the Enter key")  
         
        #Getting the final access token
        final_token = self.apps.UpgradeToOAuthAccessToken(self.requestToken)
        
        #Saving in file
        f = open("oauth.txt", 'wb')
        f.write('%s\n' % (self.domain,))
        pickle.dump(final_token, f)
        f.close()

    
