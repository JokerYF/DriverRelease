from code.common import RequestBase, JsonParser

url2 = 'https://googlechromelabs.github.io/chrome-for-testing/latest-patch-versions-per-build.json'
json_parser2 = JsonParser('../ChromeDriverLatestPatchVersion.json')

data2 = RequestBase(url2).get
if json_parser2.get('timestamp', '') != data2['timestamp']:
    json_parser2.set(data2)
    print(data2)
    print('Update ChromeDriverLatestPatchVersion.json Succeed!')
