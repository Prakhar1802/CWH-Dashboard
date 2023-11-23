"""Hello Everybody, this is an Analytical project based on python and Power-BI, I am going to perform some analytical
test on a YouTube Channel name CodeWithHarry. I am going to find some insights from this channel.

Resources Used in it In this analysis, I am going to use YouTube API, for fetching the data of the channel,
also I am going to use advance libraries of Python like pandas.

Steps for doing the analysis
In this analysis, first we are going to create the dataset of CodeWithHarry channel by the help of python and pandas.

After that I am going to do some data pre-processing for making the data more good and useful for analysis. After
that I am going to save the data in an Excel file for creating the dynamic dashboard using Power-BI"""

from googleapiclient.discovery import build
from channel_status import get_channel_stats
from videoId import get_video_id
from videoDetails import get_video_details

# API Keys for youtube data access
api_key = "AIzaSyARSGxtlVstkSZfyD8vL78Vb6B2iUNubFs"
channel_id = ["UCeVMnSShP_Iviwkknt83cww", ]

# Initializing the youtube API
api_service_name = "youtube"
api_version = "v3"

# Get credentials and create an API clien
youtube = build(
    api_service_name, api_version, developerKey=api_key)

# Channel Status and information
channel_stats = get_channel_stats(youtube, channel_id)
print(channel_stats)

# Getting Video Ids
playlist_id = "UUeVMnSShP_Iviwkknt83cww"
video_ids = get_video_id(youtube, playlist_id)

# Getting Video Details
video_df = get_video_details(youtube, video_ids)
print(video_df)

"""
We have a great dataset from youtube, Now we have to do some pre processing analysis and also some cleaning
"""

# Data Pre-Processing


# Null values in dataset
print("Checking Null Values in dataset")
print(video_df.isnull().any())
#
"""
In the above analysis we find that some of the columns have null values and we have to manage them the columns
are tags, videoCount, and favouriteCount.
"""

# DataTypes checking
print("Checking the datatypes of the columns of dataset")
print(video_df.dtypes)

"""
In the dataset all the columns are of object type, so we have to change some column's datatype, 
because we have  so numeric data also in the dataset.
"""

# Exporting the dataset to excel
print("Importing the data to excel file......")
video_df.to_excel("C:\\Users\\prakh\\Downloads\\Practice DataSet\\CodeWithHarry.xlsx")