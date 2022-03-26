from utilities.configurations import open_dbConnection, getQuery


def addBookpayload(isbn, aisle):
    body = {
        "name": "Python api testing",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Nikhil shukla"
    }

    return body


def buildPayloadFromDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
