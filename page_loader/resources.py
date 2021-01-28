import requests
from page_loader.files import write_to_file
from progress.bar import Bar


def download_resources(resources):
    bar = Bar('Downloading progress', fill='*', suffix='%(percent)d%%', max=len(resources))    # noqa: E501
    for resource in resources:
        link, path_to_file = resource
        write_to_file(requests.get(link).content, path_to_file, 'wb')
        bar.next()
    bar.finish()
