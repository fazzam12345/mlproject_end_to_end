import sys
import logging

def error_message_detail(error, error_detail: sys.exc_info) -> str:
    '''
    This function will return the error message detail
    '''
    _, _, exec_tb = error_detail
    error_message = f"Error occurred in line {exec_tb.tb_lineno} in file {exec_tb.tb_frame.f_code.co_filename}, error message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys.exc_info):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info(CustomException("Divide by zero error", error_detail=sys.exc_info()))
        raise CustomException(str(e), sys.exc_info()) from e
