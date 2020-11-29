#!/usr/bin/env python

from ..common import *
from ..extractor import VideoExtractor

def streamye_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    vids = re.findall('https://streamye.com/([^"]*)', url)
    html = get_content(url, headers=fake_headers)
    video_urls = re.findall(r'src="https://cdnye.streamye.com/([^"]*)"', html)
    if len(video_urls) > 0 and len(vids) == 1:
        url = 'https://cdnye.streamye.com/%s' % video_urls[0]
        _, ext, size = url_info(url, faker=True)
        title = "streamaye_%s" % vids[0]
        if not info_only:
            download_urls([url], title, ext, size, output_dir=output_dir, merge=merge, faker=True)
    return

site_info = "streamye.com"
download = streamye_download
download_playlist = playlist_not_supported('streamye')
