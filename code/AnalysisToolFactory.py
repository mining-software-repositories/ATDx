from SonarCloudTool import *


class AnalysisToolFactory:
    def __init__(self):
        self.factory_tool = {
            "SonarCloud": SonarCloudTool,
        }

    def get_analysis_tool(self, analyis_tool, n, portfolio_info, suffix):
        if analyis_tool in self.factory_tool:
            tool_to_return = self.factory_tool[analyis_tool]
            return tool_to_return(n, portfolio_info, suffix)
        else:
            print("The analysis tool doesn't exist. The available ones are:")
            for keys in self.factory_tool:
                print(keys)
