# Copyright 2026 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "EDI product endpoint integration",
    "summary": """
        Glue module between edi_product_oca and edi_endpoint_oca.
    """,
    "version": "18.0.1.0.0",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "maintainers": ["simahawk"],
    "website": "https://github.com/OCA/edi-framework",
    "depends": [
        "edi_product_oca",
        "edi_endpoint_oca",
    ],
    "data": [
        "views/product_views.xml",
        "views/product_packaging_views.xml",
    ],
    "auto_install": True,
}
