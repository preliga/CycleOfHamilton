
import matplotlib.pyplot as plt
import networkx as nx

class GraphPlot:

    def drawGraphPlot(self, _graph, _cycle):

        G = nx.DiGraph()

        for top in _graph.getTops():
            G.add_nodes_from(str(top.getKey()))
            for arc in top.getArcs():
                G.add_edges_from([(str(arc.getFrom()), str(arc.getTo()))], weight=arc.getValue())

        pos = nx.circular_layout(G)

        # nodes
        nx.draw_networkx_nodes(G,pos,
                               nodelist=_graph.getTopsList(),
                               node_color='r',
                               node_size=500,
                           alpha=0.8)

        # edges
        nx.draw_networkx_edges(G,pos,width=0.8,alpha=0.5,style = 'dashdot')

        # labels ednge
        edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels, label_pos=0.3)

        # hamilton cycle
        if _cycle.isCycle():
            nx.draw_networkx_edges(G,pos,
                                   edgelist=_cycle.getCyclePars(),
                                   width=2,alpha=0.5,edge_color='b')
            nx.draw_networkx_nodes(G,pos,
                                   nodelist=[str(_cycle.getStart().getKey())],
                                   node_color='y',
                                   node_size=500,
                               alpha=0.8)


        nx.draw_networkx_labels(G,pos,_graph.getTopsLabel(),font_size=12)
        plt.title('GRAF (cykl hamiltona)', fontsize=15)

        if _cycle.isCycle():
            plt.text(0, -1.2, 'Wartość cyklu: %d' % (_cycle.getValue()),
                    verticalalignment='bottom', horizontalalignment='right',
                    color='green', fontsize=15)
        else:
            plt.text(0, -1.2, 'Brak cyklu hamiltona',
                     verticalalignment='bottom', horizontalalignment='right',
                     color='green', fontsize=15)

        plt.axis('off')
        plt.savefig("labels_and_colors.png") # save as png
        plt.show() # display