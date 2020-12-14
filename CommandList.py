class CommandList:
  
  def __init__(self) -> None:
      super().__init__()
      self.commandList = {
        "appsite -version/-v/--v":                              "To check the version of AppSite",
        "appsite -help":                                        "To open cheat sheet",
        "appsite --update/--update <version_tag>":              "To update AppSite/Updating AppSite to a specific version using a version_tag",
        "appsite -github":                                      "To open github repository of AppSite",
        "appsite -documentation":                               "To see documentation of AppSite",
        "appsite -website":                                    "To open AppSite's main website",
        "appsite -help--documentation '<problem_type>'":        "To search online documentation for a particular problem or issue",
      }
      
  def getCommandListForHelp(self):
    # print(self.commandList)
    
    self.commandTitle = list(self.commandList.keys())
    self.commandDescription = list(self.commandList.values())
    
    if len(self.commandTitle) == len(self.commandDescription):
      for commands in range(len(self.commandTitle)):
        print("{}\t\t\t\t-\t\t\t\t\t\t{}".format(self.commandTitle[commands], self.commandDescription[commands]))