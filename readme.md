# Alevin - Autofleet

## Utile

Odoo2026$$$

## Commandes utiles

### Docker

docker compose up -d\
docker \
docker restart odoo18-app

()\
docker compose restart odoo\
docker exec -it odoo18-app odoo -u fleet_workshop -d odoo18-db --stop-after-init\

### Windows

mkdir addons\fleet_workshop\models\
mkdir addons\fleet_workshop\views\
mkdir addons\fleet_workshop\security\
mkdir addons\fleet_workshop\data\
type nul > addons\fleet_workshop\__init__.py\
type nul > addons\fleet_workshop\__manifest__.py\
type nul > addons\fleet_workshop\models\__init__.py\
type nul > addons\fleet_workshop\models\vehicle.py\
type nul > addons\fleet_workshop\models\intervention.py\
type nul > addons\fleet_workshop\views\vehicle_views.xml\
type nul > addons\fleet_workshop\views\intervention_views.xml\
type nul > addons\fleet_workshop\security\ir.model.access.csv\
