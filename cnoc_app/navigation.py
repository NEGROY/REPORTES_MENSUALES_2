from django.urls import reverse, NoReverseMatch


MENU_CONFIG = [
    {
        "label": "Inicio",
        "url_name": "home",
        "target_blank": False,
        "children": [],
    },
    {
        "label": "Escalación",
        "url_name": None,
        "href": "#",
        "target_blank": False,
        "children": [
            {
                "label": "Tablas de Escalación",
                "url_name": "escalacion:tableroEscalacion",
                "target_blank": False,
            },
            {
                "label": "Tablero",
                "url_name": "escalacion:tablero",
                "target_blank": False,
            },
            {
                "label": "Fallas Asociadas",
                "url_name": "escalacion:fallas_asociadas",
                "target_blank": False,
            },
        ],
    },
    {
        "label": "Asignación de Asientos",
        "url_name": None,
        "href": "#",
        "target_blank": False,
        "children": [],
    },
    {
        "label": "Retroalimentación",
        "url_name": None,
        "href": "#",
        "target_blank": False,
        "children": [],
    },
]


def _resolve_href(item):
    url_name = item.get("url_name")
    fallback = item.get("href", "#")

    if not url_name:
        return fallback

    try:
        return reverse(url_name)
    except NoReverseMatch:
        return fallback


def build_navigation():
    menu = []

    for item in MENU_CONFIG:
        children = item.get("children", [])

        built_item = {
            "label": item["label"],
            "href": _resolve_href(item),
            "target_blank": item.get("target_blank", False),
            "children": [],
        }

        for child in children:
            built_item["children"].append({
                "label": child["label"],
                "href": _resolve_href(child),
                "target_blank": child.get("target_blank", False),
            })

        menu.append(built_item)

    return menu