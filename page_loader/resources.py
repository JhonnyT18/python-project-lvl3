import requests
from page_loader.files import write_to_file


def download_resources(resources):
    for resource in resources:
        link, path_to_file = resource
        write_to_file(requests.get(link).content, path_to_file, 'wb')
