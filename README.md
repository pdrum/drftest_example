DRF TEST Example
---------------

This project is a demonstration of how **DRF Test** can be used for simplifying writing tests
and documentation for APIs developed using django-rest-framework. 

**DRF Test** can be accessed using:

* Pypi: https://pypi.org/project/drftest/
* Github: https://github.com/pdrum/drftest
* Documentation demo: https://drftest.netlify.com/


The project consists of a very simple django app which exposes APIs for creating
todo-items. Of course in order to make that work there are some models, serializers, etc
as well. The tests are in `todo/tests/test_view.py` and source for generated documentation 
resides at `generated_docs/` directory. The resulting documentation is also hosted on 
netlify and can be accessed using [this link](https://drftest.netlify.com/)
