# Inventory Project Backend

## Install Django

`pip install Django`

## Startup

```bash
cd inventory_project
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Tables to Implement

### Current Inventory Table

Holds information for the current inventory including item description, 
amount of each item, and total value.

### Sales

Holds information for the sales and adjust the inventory based on the
quantity of sales.

### Production

Holds information on the inputs produced and updates the current 
inventory accordingly.

### Logs
Holds information on each edit to the tables. (**may be changed later**)

## API's

### Inventory Managment

#### `GET` Current Inventory
**/api/inventoryManagment/currentInventory?user=<USER_NAME>**

**TODO** - switch to some sort of OAuth implementation later on

Response:

```json
{
   "data":[
      {
         "inventoryID":"NUMBER",
         "name":"STRING",
         "unitPrice":"NUMBER",
         "quantity":"NUMBER",
         "inventoryValue":"NUMBER",
         "minimalSupply":"NUMBER"
      }
   ]
}
```

#### `POST` Add Inventory Item
**/api/inventoryManagment/addInventoryItem?user=<USER_NAME>**

**TODO** - switch to some sort of OAuth implementation later on

Request:
```json
{
  "data":{
         "name":"STRING",
         "unitPrice":"NUMBER",
         "quantity":"NUMBER",
         "minimalSupply":"NUMBER"
  }
}
```

Response:
`HTTP: 200` OR `HTTP: 400`

#### `PUT` Update Inventory Item
**/api/inventoryManagment/updateInventoryItem?user=<USER_NAME>**

**TODO** - switch to some sort of OAuth implementation later on

Request:
```json
{
  "data":{
        "inventoryID":"NUMBER",
         "name":"STRING",
         "unitPrice":"NUMBER",
         "quantity":"NUMBER",
         "minimalSupply":"NUMBER"
  }
}
```

Response:
`HTTP: 200` OR `HTTP: 400`
