
#include <vector>
#include <map>
#include <pthread.h>


struct Node {

    double range;
    int id;
    int cluster_id;
    bool active;
    std::vector<double> pos;

    Node() : range(0), id(0), cluster_id(0), active(true) {}
    Node(double& r, double& i, double& c_i) : range(r), id(i), cluster_id(c_i), active(true) {}

};


struct Graph {

    int n;
    std::vector<Node> nodes;
    std::vector<std::vector<Node>> adj;
    std::map<int, int> group_ids; // group_ids[id] = cluster_id
    std::vector<int> group_count; // count of cluster per group

    void change_id(Node* node, int& to_change, int& new_id) {
        if (node->cluster_id == to_change) {
            node->cluster_id = new_id;
        }
        return;
    }

    void change_node_ids(int& to_change, int& new_id) {

        // change ids
        pthread_t threads[group_count[to_change]];
        
        for (int i = 0; i < group_count[to_change]; ++i) {
            
        }


        // update count


    }

};



