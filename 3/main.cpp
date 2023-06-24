#include <unordered_map>
#include <string>
#include <fstream>
#include <sstream>
#include "vector"

using namespace std;

const std::string Symbols = ",;.:-()\t!¡¿?\"[]{}&<>+-*/=#'";

int helper(vector<pair<int, string>>& f, int l, int r) {
    int pi = f[r].first;
    int i = l;

    for (int j=l; j<r; j++)
        if (f[j].first > pi)
            swap(f[j], f[i++]);

    swap(f[r], f[i]);

    return i;
}


int dnc(vector<pair<int,string>>& f, int k, int l, int r) {
    if (l<=r) {
        int pi = helper(f, l, r);
        if (pi+1 == k) return pi;
        else if (pi+1 > k) return dnc(f, k, l, pi-1);
        else return dnc(f, k, pi+1, r);
    }

    return -1;
}



vector<string> topKFrequent(std::istream &in, int k) {
    unordered_map<string, int> mp;
    std::string line;
    std::string word;
    while( std::getline( in, line ) ) {
        // Substitute punctuation symbols with spaces
        for (std::string::iterator it = line.begin(); it != line.end(); ++it) {
            if (Symbols.find(*it) != std::string::npos) {
                *it = ' ';
            }

        }

        // Let std::operator>> separate by spaces
        std::istringstream filter(line);
        while (filter >> word) {
            mp[word]++;
        }
    }

    vector<pair<int, string>> f;
    for (auto i: mp) f.push_back({i.second, i.first});

    int idx = dnc(f, k, 0, f.size()-1);

    vector<string> ans;
    for (int i=0; i<=idx; i++)
        ans.push_back(f[i].second);

    return ans;
}


int main() {
    std::ifstream fin("input.txt");
    auto result = topKFrequent(fin, 10);
    for (auto st: result) {
        printf("%s\n", st.c_str());
    }
}