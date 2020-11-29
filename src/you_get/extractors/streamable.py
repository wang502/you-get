#!/usr/bin/env python

from ..common import *
from ..extractor import VideoExtractor

def streamable_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    vids = re.findall('https://streamable.com/([^"]*)', url)
    html = get_content(url, headers=fake_headers)
    video_urls = re.findall(r'src="//cdn-cf-east.streamable.com/video/([^"]*)"', html)
    print(video_urls)
    if len(video_urls) > 0 and len(vids) == 1:
        url = 'https://cdn-cf-east.streamable.com/video/%s' % video_urls[0]
        print(url)
        type, ext, size = url_info(url, faker=True)
        title = "streamable_%s" % vids[0]
        if not info_only:
            download_urls([url], title, ext, size, output_dir=output_dir, merge=merge, faker=True)

site_info = "streamable.com"
download = streamable_download
download_playlist = playlist_not_supported('streamable')
