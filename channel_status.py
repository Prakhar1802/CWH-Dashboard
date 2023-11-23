import pandas as pd


def get_channel_stats(youtube, channel_id):
    all_data = []
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=",".join(channel_id)
    )
    response = request.execute()

    # loop through items
    for item in response["items"]:
        data = {
            "channelName": item["snippet"]["title"],
            "subscriber": item["statistics"]["subscriberCount"],
            "views": item["statistics"]["viewCount"],
            "totalViews": item["statistics"]["videoCount"],
            "playlistId": item["contentDetails"]["relatedPlaylists"]["uploads"]
        }
        all_data.append(data)
        return pd.DataFrame(all_data)
