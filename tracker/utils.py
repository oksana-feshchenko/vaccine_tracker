def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        referer = '/'
    return referer


def get_vaccine_id_from_url(url):
    split_url = url.split("/")
    if len(split_url) >= 8:
        return split_url[-4]
    elif len(split_url) == 7:
        return split_url[-3]
    else:
        return split_url[-2]
