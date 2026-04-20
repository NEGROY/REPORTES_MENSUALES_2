from .navigation import build_navigation


def cnoc_navigation(request):
    return {
        "cnoc_menu": build_navigation(),
    }