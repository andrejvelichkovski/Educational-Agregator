# Python script that fetches data from 15 different channels 
# and saves the data in separate JSON files
# This script could be run on each 24 hours, in order to avoid
# making too much API calls which can often be expensive and limited
# and the videos data doesn't change a lot
import requests
import json

# API constants
API_KEY = 'X'
API_LINK = 'https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId='
FILE_ADDRESS = 'resources/videos_data/'

# Channel informations
video_categories = ['science', 'tech', 'math', 'travel']
channel_ids = [
    [
        "UCUHW94eEFW7hkUMVaZz4eDg",
        "UCeiYXex_fwgYDonaTcSIk6w",
        "UCHnyfMqiRRG1u-2MsSQLbXA",
        "UC6nSFpj9HTCZ5t-N3Rm3-HA",
        "UC6107grRI4m0o2-emgoDnAA",
        "UCxqAWLTk1CmBvZFPzeZMd9A"
    ],
    [
        "UC0vBXGSyV14uvJ4hECDOl0Q",
        "UCVLZmDKeT-mV4H3ToYXIFYg"
    ],
    [
        "UCoxcjq-8xIDTYp3uz647V5A",
        "UCHnj59g7jezwTy5GeL8EA_g",
        "UConVfxXodg78Tzh5nNu85Ew",
        "UCYO_jab_esuFRV4b17AJtAw"
    ],
    [
        "UCmmPgObSUPw1HL2lq6H4ffA",
        "UC_DmOS_FBvO4H27U7X0OtRg",
        "UCckFCPnDSf9mMCkdEq7tTcQ",
        "UCs5GnuB9y1pSWswQPLF2kXA"
    ]
]

# For each channel in each category we store the data in separate JSON file
for i in range(len(video_categories)):
    for j in range(len(channel_ids[i])):
        current_channel_id = channel_ids[i][j]
        url = API_LINK + current_channel_id + '&maxResults=50&key=' + API_KEY
        
        response = requests.request("GET", url)

        current_file_link = FILE_ADDRESS + video_categories[i] + str(j) + '.json'
        with open(current_file_link, 'w') as fp:
            json.dump(response.json(), fp)