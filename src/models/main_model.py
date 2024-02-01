"""
    MongoEngine converts class names to collection names by converting the class name from CamelCase to snake_case.
    For example, the class name BlogPost will be converted to the collection name blog_posts.
    If you want to override this behavior, you can specify a custom collection name by setting the meta attribute on the class.
    For example, the following class will be stored in the collection named blog_posts:
    class BlogPost(db.Document):
        title = db.StringField()
        content = db.StringField()
        meta = {'collection': 'blog_posts'}

"""


class StatusCodeEnums:
    """Global status code enums
    This class is a model for status code enums
    main usage is with the following ResponseModel class

    succes should be returned when the request is successful
    not_found should be returned when the requested resource or data is not found
    bad_request should be returned when the request is not valid
    unauthorized should be returned when the user is not authorized to access the requested resource
    gone should be returned when the requested resource is no longer available

    """
    success = {"msg": "Success", "code": 200}
    not_found = {"msg": "Not found", "code": 404}
    bad_request = {"msg": "Bad Request", "code": 400}
    unauthorized = {"msg": "Unauthorized", "code": 401}
    gone = {"msg": "Gone", "code": 410}


# ----------------------------------------------------


class ResponseModel:
    """This class is a global model for response model

    Parameters
    ----------
        data: MongoEngine object
            data to be returned

    Returns
    -------
        get_success_response
            returns a success response with "success" message and 200 status code
        get_not_found_response
            returns a not found response with "not found" message and 404 status code
        get_bad_request_response
            returns a bad request response with "bad request" message and 400 status code
        get_unauthorized_response
            returns a unauthorized response with "unauthorized" message and 401 status code
    """

    def __init__(self, data=None):
        # *The constructor for ResponseModel class
        
        self.data = data

    # only this response will return data with success message and 200 status code
    def get_success_response(self):
        return ({
            "msg": StatusCodeEnums.success["msg"],
            "data": self.data
        }, StatusCodeEnums.success["code"])

    def get_not_found_response(self):
        # return a not found response with "not found" message and 404 status code
        return ({
            "msg": StatusCodeEnums.not_found["msg"],
        }, StatusCodeEnums.not_found["code"])

    def get_bad_request_response(self):
        # return a bad request response with "bad request" message and 400 status code
        return ({
            "msg": StatusCodeEnums.bad_request["msg"],
        }, StatusCodeEnums.bad_request["code"])

    def get_unauthorized_response(self):
        # return a unauthorized response with "unauthorized" message and 401 status code
        return ({
            "msg": StatusCodeEnums.unauthorized["msg"],
        }, StatusCodeEnums.unauthorized["code"])