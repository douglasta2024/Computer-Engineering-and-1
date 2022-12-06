import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph(): #Builds the graph
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y): #Function to display graph
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Overall Progress')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Day')
    plt.ylabel('Miles')
    plt.tight_layout()
    graph = get_graph()
    return graph