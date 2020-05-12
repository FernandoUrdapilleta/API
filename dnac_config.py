'''

To set and get environment variables in Python you can just use the os module.

Environment variables are useful when you want to avoid hard-coding access credentials or other variables into code.
For example, you may need to pass in API credentials for DNAC to make changes but you wouldn’t want these credentials
stored in your code repository. Or perhaps you need your code to function slightly differently between your development,
staging and production environments. In this case you could pass in an environment variable to tell your application
what environment it’s running in.

'''
import os

DNAC=os.environ.get('DNAC','sandboxdnac.cisco.com')
DNAC_PORT=os.environ.get('DNAC_PORT',443)
DNAC_USER=os.environ.get('DNAC_USER','devnetuser')
DNAC_PASSWORD=os.environ.get('DNAC_PASSWORD','Cisco123!')

# print(DNAC)
# print(DNAC_PORT)
# print(DNAC_USER)
# print(DNAC_PASSWORD)
# print(os.environ)