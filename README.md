# Department application
## About
It is simple application which provides you an ability to manage departments and employees.
You can perform this actions using web UI or REST API:
- Create department/employee
- Update department/employee
- Delete department/employee
- View department/employee
- Filter employees by birthdate
- Get average salary by department
## Installation guide
1. Clone repo
    > git clone https://github.com/nazarkychma/department_app.git
2. Create virtual environment in project folder
    > python3 -m venv ./venv
3. Activate venv
    > source venv/bin/activate
4. Install requirements
    > pip install -r requirements.txt
5. Provide DB URL and session key in environmental variables.
   Replace values.
    > export db_uri=postgresql://dep:dep@localhost:5432/mydatabase
    > export session_key=supersecretkey 
6. Create tables using flask migrate
    > flask db upgrade
7. Run an application using gunicorn
    > gunicorn --bind 0.0.0.0:5000 app:app

## API documentation
### Departments API
* ### Get all departments
    ***
    ### Endpoint:
    ` http://{server adress}/api/department `
    ### Protocol:
    ` GET `

    #### Request example:
	```shell
    curl --location --request GET 'http://127.0.0.1:5000/api/department'
	```
 
    #### Response example:

	200 OK
	
	```json
    {
    "departments": [
        {
            "avg_salary": 100.0,
            "employees": [
                {
                    "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
                    "department_id": 1,
                    "department_name": "Test1",
                    "id": 1,
                    "name": "Test Test",
                    "salary": 100.0
                },
                {
                    "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
                    "department_id": 1,
                    "department_name": "Test1",
                    "id": 5,
                    "name": "Test Test",
                    "salary": 100.0
                }
            ],
            "id": 1,
            "name": "Test1",
            "num_of_employees": 2
        },
        {
            "avg_salary": 100.0,
            "employees": [
                {
                    "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
                    "department_id": 2,
                    "department_name": "Test2",
                    "id": 2,
                    "name": "Test Test",
                    "salary": 100.0
                }
            ],
            "id": 2,
            "name": "Test2",
            "num_of_employees": 1
        }
      ]
    }
    ```
 
* ### Create department
	***
	#### Endpoint:
	` http://{server adress}/api/department `
	#### Protocol:
    ` POST `
	#### Body:
	```json
	{
	    "name": "{department-name}"
	}
	```

	#### Request example:
	```shell
    curl --location --request POST 'http://127.0.0.1:5000/api/department' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "name": "{{random_name}}"
    }'
	```

	#### Response example:

	201 Created

	```json
    {
      "id": 5
    }
	```
 * ### Delete department
	***
	#### Endpoint:
	` http://{server adress}/api/department/{department id} `
	#### Protocol:
    ` DELETE `

	#### Request example:
	```shell
    curl --location --request DELETE 'http://127.0.0.1:5000/api/department/5'
	```
	#### Response example:

	200 OK

	```json
    {
      "Deleted": true
    }
	```
 
 * ### Get department
	***
	#### Endpoint:
	` http://{server adress}/api/department/{department id} `
	#### Protocol:
    ` GET `

	#### Request example:
	```shell
    curl --location --request GET 'http://127.0.0.1:5000/api/department/1'
	```
	#### Response example:

	200 OK

	```json
    {
    "avg_salary": 100.0,
    "employees": [
        {
            "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
            "department_id": 1,
            "department_name": "Test1",
            "id": 1,
            "name": "Test Test",
            "salary": 100.0
        },
        {
            "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
            "department_id": 1,
            "department_name": "Test1",
            "id": 5,
            "name": "Test Test",
            "salary": 100.0
        }
    ],
    "id": 1,
    "name": "Test1",
    "num_of_employees": 2
    }
	```
 * ### Update department
	***
	#### Endpoint:
	` http://{server adress}/api/department/{department id} `
	#### Protocol:
    ` PATCH `
	#### Body:
	```json
	{
	    "name": "{department-name}"
	}
	```

	#### Request example:
	```shell
    curl --location --request PATCH 'http://127.0.0.1:5000/api/department/1' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "name": "{{random_name}}"
    }'
	```

	#### Response example:

	200 OK

	```json
    {
    "Updated": {
        "avg_salary": 100.0,
        "employees": [
            {
                "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
                "department_id": 1,
                "department_name": "Postmant532",
                "id": 1,
                "name": "Test Test",
                "salary": 100.0
            },
            {
                "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
                "department_id": 1,
                "department_name": "Postmant532",
                "id": 5,
                "name": "Test Test",
                "salary": 100.0
            }
        ],
        "id": 1,
        "name": "Postmant532",
        "num_of_employees": 2
      }
    }
	```
 ### Employees API
 * ### Get all employees
    ***
    ### Endpoint:
    ` http://{server adress}/api/employee `
    ### Protocol:
    ` GET `

    #### Request example:
    ```shell
    curl --location --request GET 'http://127.0.0.1:5000/api/employee'
    ```
 
    #### Response example:

    200 OK
	
    ```json
    {
    "employees": [
        {
            "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
            "department_id": 1,
            "department_name": "Postmant532",
            "id": 1,
            "name": "Test Test",
            "salary": 100.0
        },
        {
            "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
            "department_id": 2,
            "department_name": "Test2",
            "id": 2,
            "name": "Test Test",
            "salary": 100.0
        },
        {
            "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
            "department_id": 3,
            "department_name": "Test3",
            "id": 3,
            "name": "Test Test",
            "salary": 100.0
        },
        {
            "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
            "department_id": 1,
            "department_name": "Postmant532",
            "id": 5,
            "name": "Test Test",
            "salary": 100.0
        },
        {
            "birthdate": "Wed, 05 Jan 2022 00:00:00 GMT",
            "department_id": 4,
            "department_name": "TestCreate",
            "id": 4,
            "name": "test Test",
            "salary": 5.0
        }
      ]
    }
    ```
 
 * ### Create employee
     ***
     #### Endpoint:
     ` http://{server adress}/api/employee `
     #### Protocol:
     ` POST `
     #### Body:
     ```json
     {
       "first_name": "{first name}",
       "last_name": "{last name}",
       "salary": "{salary}",
       "department_id": "{department id}",
       "birthdate": "{birthdate}"
     }
     ```

     #### Request example:
     ```shell
     curl --location --request POST 'http://127.0.0.1:5000/api/employee' \
     --header 'Content-Type: application/json' \
     --data-raw '{
     "first_name": "{{first_name}}",
     "last_name": "{{last_name}}",
     "salary": {{salary}},
     "department_id": 1,
     "birthdate": "2018-01-01"
     }'
     ```

     #### Response example:

     201 Created

     ```json
     {
       "birthdate": "Mon, 01 Jan 2018 00:00:00 GMT",
       "department_id": 1,
       "department_name": "Postmant532",
       "id": 6,
       "name": "Holden MacGyver",
       "salary": 911.0
     }
     ```
 
 * ### Get employee
    ***
    #### Endpoint:
    ` http://{server adress}/api/employee/{employee id} `
    #### Protocol:
    ` GET `

    #### Request example:
    ```shell
    curl --location --request GET 'http://127.0.0.1:5000/api/employee/1'
    ```
    #### Response example:

    200 OK

    ```json
    {
      "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
      "department_id": 1,
      "department_name": "Postmant532",
      "id": 1,
      "name": "Test Test",
      "salary": 100.0
    }
    ```
 
 * ### Delete employee
    ***
    #### Endpoint:
    ` http://{server adress}/api/employee/{employee id} `
    #### Protocol:
    ` DELETE `

    #### Request example:
    ```shell
    curl --location --request DELETE 'http://127.0.0.1:5000/api/employee/6'
    ```
    #### Response example:

    200 OK

    ```json
    {
    "Deleted": {
        "birthdate": "Mon, 01 Jan 2018 00:00:00 GMT",
        "department_id": 1,
        "department_name": "Postmant532",
        "id": 6,
        "name": "Holden MacGyver",
        "salary": 911.0
    }
   }
    ```
 
 * ### Update employee
     ***
     #### Endpoint:
     ` http://{server adress}/api/employee/{employee id} `
     #### Protocol:
     ` PATCH `
     #### Body:
     ```json
     {
       "first_name": "{first name OPTIONAL}",
       "last_name": "{last name OPTIONAL}",
       "salary": "{salary OPTIONAL}",
       "department_id": "{department id OPTIONAL}",
       "birthdate": "{YYYY-MM-DD OPTIONAL}"
     }
     ```

     #### Request example:
     ```shell
     curl --location --request PATCH 'http://127.0.0.1:5000/api/employee/1' \
     --header 'Content-Type: application/json' \
     --data-raw '{
     "salary": {{salary}},
     "department_id": 2,
     "birthdate": "2019-01-01"
     }'
     ```

     #### Response example:

     200 OK

     ```json
     {
     "Updated": {
         "birthdate": "Tue, 01 Jan 2019 00:00:00 GMT",
         "department_id": 2,
         "department_name": "Test2",
         "id": 1,
         "name": "Test Test",
         "salary": 294.0
      }
     }
     ```
 
 * ### Filter employees by birthdate
    ***
    #### Endpoint:
    ` http://{server adress}/api/employee/filter `
    #### Protocol:
    ` GET `
    #### Query params:
    ```text
    from_date - required
    to_date - optional, if provided all employees, who were born between from_date and to_date will be returned
    ```
    #### Request example:
    ```shell
    curl --location --request GET 'http://127.0.0.1:5000/api/employee/filter?from_date=2019-01-01'
    ```
    #### Response example:

    200 OK

    ```json
    {
    "employees": [
        {
            "birthdate": "Tue, 01 Jan 2019 00:00:00 GMT",
            "department_id": 2,
            "department_name": "Test2",
            "id": 1,
            "name": "Test Test",
            "salary": 294.0
        }
      ]
    }
    ```
    #### Request example:
    ```shell
    curl --location --request GET 'http://127.0.0.1:5000/api/employee/filter?from_date=2019-01-01&to_date=2023-01-01'
    ```
    #### Response example:

    200 OK

    ```json
    {
    "employees": [
        {
            "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
            "department_id": 2,
            "department_name": "Test2",
            "id": 2,
            "name": "Test Test",
            "salary": 100.0
        },
        {
            "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
            "department_id": 3,
            "department_name": "Test3",
            "id": 3,
            "name": "Test Test",
            "salary": 100.0
        },
        {
            "birthdate": "Tue, 04 Jan 2022 00:00:00 GMT",
            "department_id": 1,
            "department_name": "Postmant532",
            "id": 5,
            "name": "Test Test",
            "salary": 100.0
        },
        {
            "birthdate": "Wed, 05 Jan 2022 00:00:00 GMT",
            "department_id": 4,
            "department_name": "TestCreate",
            "id": 4,
            "name": "test Test",
            "salary": 5.0
        },
        {
            "birthdate": "Tue, 01 Jan 2019 00:00:00 GMT",
            "department_id": 2,
            "department_name": "Test2",
            "id": 1,
            "name": "Test Test",
            "salary": 294.0
        }
      ]
    }
    ```