class PostedDataValidation:
    def checkPostedData(postedData, functionName):
        if functionName == "Addition" or functionName == "Subtraction" or functionName == "Multiplication":
            if "x" not in postedData or "y" not in postedData:
                return 301
            else:
                return 200
        elif functionName ==  "Division":
            if "x" not in postedData or "y" not in postedData:
                return 301
            elif int(postedData["y"]) <= 0:
                return 302
            else:
                return 200