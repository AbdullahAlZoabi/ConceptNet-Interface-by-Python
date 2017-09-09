import requests


class Edge:
    StartNode = ""
    EndNode = ""
    Relation = ""
    Weight = 0
    SurfaceText = ""


    def Set_StartNode(self,lable):
        self.StartNode = lable

    def Get_StartNode(self):
        return self.StartNode

    def Set_EndNode(self,lable):
        self.EndNode = lable

    def Get_EndNode(self):
        return self.EndNode

    def Set_Relation(self,relation):
        self.Relation = relation

    def Get_Relation(self):
        return self.Relation

    def Set_Weight(self,weight):
        self.Weight = weight

    def Get_Weight(self):
        return self.Weight

    def Set_SurfaceText(self,surfacetext):
        self.SurfaceText = surfacetext

    def Get_SurfaceText(self):
        return self.SurfaceText




    
def GetAllEdges(node_label,MinWeight,MaxNumOfEdges,LabelIsStartOnly):

    ProcessedEdges = []
    
    URL = 'http://api.conceptnet.io/c/en/' + node_label +'?offset=0&limit=1000000'

    RawData = requests.get(URL).json()

    RawEdges = RawData['edges']

    Counter = 0

    for edge in RawEdges:

        Weight = edge['weight']
        Start = edge['start']['label']
        
        if (Counter < MaxNumOfEdges and Weight >= MinWeight and ((Start == node_label) or not LabelIsStartOnly) ):
            temp = Edge()
            temp.Set_StartNode(edge['start']['label'])
            temp.Set_EndNode(edge['end']['label'])
            temp.Set_Relation(edge['rel']['label'])
            temp.Set_Weight(edge['weight'])
            temp.Set_SurfaceText(edge['surfaceText'])
            ProcessedEdges.append(temp)
            Counter = Counter + 1
        
    return ProcessedEdges





def GetEdges(start_label,end_label,MinWeight,MaxNumOfEdges):

    ProcessedEdges = []
    
    URL = 'http://api.conceptnet.io/c/en/' + start_label +'?offset=0&limit=1000000'

    RawData = requests.get(URL).json()

    RawEdges = RawData['edges']

    Counter = 0

    for edge in RawEdges:

        Weight = edge['weight']
        Start = edge['start']['label']
        end = edge['end']['label']
        
        if (Counter < MaxNumOfEdges and Weight >= MinWeight and Start==start_label and end==end_label):
            temp = Edge()
            temp.Set_StartNode(edge['start']['label'])
            temp.Set_EndNode(edge['end']['label'])
            temp.Set_Relation(edge['rel']['label'])
            temp.Set_Weight(edge['weight'])
            temp.Set_SurfaceText(edge['surfaceText'])
            ProcessedEdges.append(temp)
            Counter = Counter + 1
        
    return ProcessedEdges





def GetEdgesEnd(start_label,relation,MinWeight,MaxNumOfEdges):

    ProcessedEdges = []
    
    URL = 'http://api.conceptnet.io/c/en/' + start_label +'?offset=0&limit=1000000'

    RawData = requests.get(URL).json()

    RawEdges = RawData['edges']

    Counter = 0

    for edge in RawEdges:

        Weight = edge['weight']
        Start = edge['start']['label']
        Relation = edge['rel']['label']
        
        if (Counter < MaxNumOfEdges and Weight >= MinWeight and Start == start_label and Relation== relation):
            temp = Edge()
            temp.Set_StartNode(edge['start']['label'])
            temp.Set_EndNode(edge['end']['label'])
            temp.Set_Relation(edge['rel']['label'])
            temp.Set_Weight(edge['weight'])
            temp.Set_SurfaceText(edge['surfaceText'])
            ProcessedEdges.append(temp)
            Counter = Counter + 1
        
    return ProcessedEdges





def GetEdgesStart(end_label,relation,MinWeight,MaxNumOfEdges):

    ProcessedEdges = []
    
    URL = 'http://api.conceptnet.io/c/en/' + end_label +'?offset=0&limit=1000000'

    RawData = requests.get(URL).json()

    RawEdges = RawData['edges']

    Counter = 0

    for edge in RawEdges:

        Weight = edge['weight']
        End = edge['end']['label']
        Relation = edge['rel']['label']
        
        if (Counter < MaxNumOfEdges and Weight >= MinWeight and End == end_label and Relation == relation):
            temp = Edge()
            temp.Set_StartNode(edge['start']['label'])
            temp.Set_EndNode(edge['end']['label'])
            temp.Set_Relation(edge['rel']['label'])
            temp.Set_Weight(edge['weight'])
            temp.Set_SurfaceText(edge['surfaceText'])
            ProcessedEdges.append(temp)
            Counter = Counter + 1
        
    return ProcessedEdges





def GetDistRelations(edges):

    DistRelations = set()

    for edge in edges:
        DistRelations.add(edge.Get_Relation())


    return list(DistRelations)





def GetEdgesByRelation(edges,relation):

    ProcessedEdges = []

    for edge in edges:
        if(edge.Get_Relation() == relation):
                    ProcessedEdges.append(edge)

    return ProcessedEdges





