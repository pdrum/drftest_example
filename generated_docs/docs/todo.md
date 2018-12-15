

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
    "AUTHORIZATION": "Token e2a37bee2f14cc7159c02830ad1dd6c11bd1ca41"
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
    "AUTHORIZATION": "Token 46eed6a52e75c5d6dc41f6c9e6fdc513ba9134af"
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



## DeleteToDoItemViewTest



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
    "AUTHORIZATION": "Token b04b13687fe88ea15a0b1447aaf469ef19797edb"
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
    "AUTHORIZATION": "Token 68d9252f8c9d99777109f2d23257e5e47e4ca9bc"
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
    "AUTHORIZATION": "Token 6c070266b972cc84b720cb7f9129ded465e2e01c"
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
    "AUTHORIZATION": "Token f2a190162facf54ba7d9777828d39325eb0cad09"
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
    "AUTHORIZATION": "Token 40bbb0e94ba5ecff66b42a48a76a88fb5fa1df2e"
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



