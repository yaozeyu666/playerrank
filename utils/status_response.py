
class StatusResponse(object):
    @classmethod
    def success(cls, data):
        return {
                "message": "ok",
                "code": "200",
                "data": data or {},
            }

    @classmethod
    def error(cls, code, msg):
        return {
                "message": msg,
                "code": str(code),
                "data": {},
            }
