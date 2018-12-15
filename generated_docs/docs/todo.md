

# todo

todo app has the following tests.
Tests are categorized into classes where each class has
several test cases.


## CreateToDoItemTest



This endpoint creates to-do items



This class has the following test cases:



<details>
<summary>&#10004; **test_successful_creation**
</summary>


* **URL:** `/api//todo-items/`
* **Method:** `post`
* **Format:** `json`




* **Headers:** 
```json
{
    "AUTHORIZATION": "Token 77acec346c95d9b52c6f21ff16a0d4fd0c4b0567"
}
```



* **Request data:** 
```json
{
    "is_done": true,
    "name": "First"
}
```


* **Response status code**: 201


* **Response data:** 
```json
{
    "id": 1,
    "is_done": true,
    "name": "First"
}
```


</details>

<details>
<summary>&#10008; **test_without_name**
</summary>


* **Description:** 
        `name` should be provided in request body.
        

* **URL:** `/api//todo-items/`
* **Method:** `post`
* **Format:** `json`




* **Headers:** 
```json
{
    "AUTHORIZATION": "Token 0d70155b85201c3a93fa17aa3362945d7939b19c"
}
```



* **Request data:** 
```json
{
    "is_done": true
}
```


* **Response status code**: 400


* **Response data:** 
```json
{
    "name": [
        "This field is required."
    ]
}
```


</details>



## DeleteToDoItemTest



This endpoint deletes to-do items.



This class has the following test cases:



<details>
<summary>&#10004; **test_successful_deletion**
</summary>


* **URL:** `/api//todo-items/1/`
* **Method:** `delete`
* **Format:** `json`


* **Path parameters:** 
```json
{
    "pk": 1
}
```



* **Headers:** 
```json
{
    "AUTHORIZATION": "Token 151d92397ead142c4560e96a973b9b5787944aca"
}
```




* **Response status code**: 204



</details>

<details>
<summary>&#10008; **test_when_id_does_not_exist**
</summary>


* **URL:** `/api//todo-items/34536/`
* **Method:** `delete`
* **Format:** `json`


* **Path parameters:** 
```json
{
    "pk": 34536
}
```



* **Headers:** 
```json
{
    "AUTHORIZATION": "Token b17bdfb848c60ad00b193f0639eb4618452ff9c4"
}
```




* **Response status code**: 404


* **Response data:** 
```json
{
    "detail": "Not found."
}
```


</details>



## EditToDoItemTest



This endpoint edits to-do items.



This class has the following test cases:



<details>
<summary>&#10004; **test_successful_edit**
</summary>


* **URL:** `/api//todo-items/1/`
* **Method:** `put`
* **Format:** `json`


* **Path parameters:** 
```json
{
    "pk": 1
}
```



* **Headers:** 
```json
{
    "AUTHORIZATION": "Token 438e496dc18cb2fd473fc640c019397be4f6b5a7"
}
```



* **Request data:** 
```json
{
    "is_done": true,
    "name": "Bar"
}
```


* **Response status code**: 200


* **Response data:** 
```json
{
    "id": 1,
    "is_done": true,
    "name": "Bar"
}
```


</details>

<details>
<summary>&#10008; **test_when_id_does_not_exist**
</summary>


* **Description:** 
        `id` should correspond to an existing to-do item.
        

* **URL:** `/api//todo-items/53353/`
* **Method:** `put`
* **Format:** `json`


* **Path parameters:** 
```json
{
    "pk": 53353
}
```



* **Headers:** 
```json
{
    "AUTHORIZATION": "Token e006764ad2a651414caadada1e5242b185698b60"
}
```



* **Request data:** 
```json
{
    "is_done": true,
    "name": "Bar"
}
```


* **Response status code**: 404


* **Response data:** 
```json
{
    "detail": "Not found."
}
```


</details>

<details>
<summary>&#10008; **test_when_name_is_missing**
</summary>


* **Description:** 
        `name` should be provided in request body.
        

* **URL:** `/api//todo-items/1/`
* **Method:** `put`
* **Format:** `json`


* **Path parameters:** 
```json
{
    "pk": 1
}
```



* **Headers:** 
```json
{
    "AUTHORIZATION": "Token 494e90b1b1afa7814f799d0bbcb10df9b4ba5f9d"
}
```



* **Request data:** 
```json
{
    "is_done": true
}
```


* **Response status code**: 400


* **Response data:** 
```json
{
    "name": [
        "This field is required."
    ]
}
```


</details>



