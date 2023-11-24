# Vendor-Management


Vendors
Create Vendor (POST):

Endpoint: /api/vendors/
Example: "http://127.0.0.1:8000/api/vendors/"
Description: Create a new vendor.
List Vendors (GET):

Endpoint: /api/vendors/
Example: "http://127.0.0.1:8000/api/vendors/"
Description: Retrieve a list of all vendors.
Delete Vendor (DELETE):

Endpoint: /api/vendors/<id>/
Example: "http://127.0.0.1:8000/api/vendors/<id>/"
Description: Delete a vendor by ID.
Update Vendor (PUT):

Endpoint: /api/vendors/<id>/
Example: "http://127.0.0.1:8000/api/vendors/<id>/"
Description: Update a vendor by ID.
Vendor Performance (GET):

Endpoint: /api/vendors/<int:pk>/performance/
Example: "http://127.0.0.1:8000/api/vendors/<int:pk>/performance/"
Description: Retrieve performance metrics for a specific vendor.
Purchase Orders
Create Purchase Order (POST):

Endpoint: /api/purchase_orders/
Example: "http://127.0.0.1:8000/api/purchase_orders/"
Description: Create a new purchase order.
List Purchase Orders (GET):

Endpoint: /api/purchase_orders/
Example: "http://127.0.0.1:8000/api/purchase_orders/"
Description: Retrieve a list of all purchase orders.
Delete Purchase Order (DELETE):

Endpoint: /api/purchase_orders/<id>/
Example: "http://127.0.0.1:8000/api/purchase_orders/<id>/"
Description: Delete a purchase order by ID.
Update Purchase Order (PUT):

Endpoint: /api/purchase_orders/<id>/
Example: "http://127.0.0.1:8000/api/purchase_orders/<id>/"
Description: Update a purchase order by ID.
Historical Performance
Create Historical Performance (POST):

Endpoint: /api/historical_performance/
Example: "http://127.0.0.1:8000/api/historical_performance/"
Description: Create a new historical performance record.
List Historical Performance (GET):

Endpoint: /api/historical_performance/
Example: "http://127.0.0.1:8000/api/historical_performance/"
Description: Retrieve a list of all historical performance records.
Delete Historical Performance (DELETE):

Endpoint: /api/historical_performance/<id>/
Example: "http://127.0.0.1:8000/api/historical_performance/<id>/"
Description: Delete a historical performance record by ID.
Update Historical Performance (PUT):

Endpoint: /api/historical_performance/<id>/
Example: "http://127.0.0.1:8000/api/historical_performance/<id>/"
Description: Update a historical performance record by ID.
Acknowledge Purchase Order
Acknowledge Purchase Order (PUT):
Endpoint: /api/purchase_orders/<int:pk>/acknowledge/
Example: "http://127.0.0.1:8000/api/purchase_orders/<int:pk>/acknowledge/"
Description: Acknowledge a purchase order, updating acknowledgment date.
