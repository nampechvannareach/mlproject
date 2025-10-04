import sys

def get_error_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    return f"Error in file {filename}, line {exc_tb.tb_lineno}: {str(error)}"

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = get_error_detail(error, error_detail)
    
    def __str__(self):
        return self.error_message

try:
    x = 10 / 0
except Exception as e:
    raise CustomException(e, sys)
