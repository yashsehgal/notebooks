class EccentricTouch:
  def __init__(self, classname, component_id=None):
    self.classname = classname
    self.componentID = component_id
    
    if (self.classname == None):
      self.shareResponse(message="""
      ClassName is not specified. Unable to fetch any sort of data.
      ClassNotSpecifiedError
      """)
  
  def shareResponse(self, message):
    print(message)
  
  def get(self, query=None, filename=None):
    
    if query is None or filename is None:
      self.shareResponse("""
        Response from API:
        Root:[{}] has invalid classname/componentID and Query Selector
        Try using some valid credentials in order to get correct response
        Error coming from server:456, ErrorRate: Normal/Warning
        """.format(filename))
      return {            # returning JSON Object - Error Response
        "response": """
        Response from API:
        Root:[{}] has invalid classname/componentID and Query Selector
        Try using some valid credentials in order to get correct response
        Error coming from server:456, ErrorRate: Normal/Warning
        """.format(filename)
      }
    
    elif query is not None and filename is not None:
      self.query = query
      self.filename = filename
      responseMessage = """
      ___________________________________
        "response": "valid",
      ___________________________________
        "classname": {},
      ___________________________________
        "componentID": {},
      ___________________________________
        "query": {},
      ___________________________________
        "filename": {},
      ___________________________________
        "dataset": 
        ___________________________________
            "componentKey": "12345",
            "componentType": "Link Text",
            "componentCode": "linktext-updt-01-black"
        ___________________________________
        "isValid": True
      ___________________________________
      """.format(
          self.classname, self.componentID, self.query, self.filename
      )
      print(responseMessage)
      return {          # returning JSON Object - Collection Set
        "response": "valid",
        "classname": self.classname,
        "componentID": self.componentID,
        "query": self.query,
        "filename": self.filename,
        "dataset": {
          "classname": self.classname,
          "id": self.componentID,
          "componentKey": "12345",
          "componentType": "Link Text",
          "componentCode": "linktext-updt-01-black"
        },
        "isValid": True
      }
      

