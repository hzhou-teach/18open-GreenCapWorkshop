// Brian Lu
// 15 mins
//***x**x***
//
#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <limits>
#include <string>

struct item {
    int original;
    int value;
};

bool sortItems(item a, item b) {
    return a.value < b.value;
}

int main()
{
    int N, temp;
    FILE *input = fopen("sort.in", "r");
    fscanf(input, "%d", &N);
    std::vector<item> items;
    for (int i = 0; i < N; i++) {
        fscanf(input, "%d", &temp);
        items.push_back(item());
        items[i].original = i;
        items[i].value = temp;
    }
    fclose(input);
    //ヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝ
    std::sort(items.begin(), items.end(), &sortItems);

    int max = 0;
    for (int i = 0; i < N; i++) {
        max = std::max(max, std::abs(i - items[i].original));
    }
    //ヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝ
    FILE *output = fopen("sort.out", "w");
    fprintf(output, "%d\n", max+1);
    fclose(output);

    return 0;
}