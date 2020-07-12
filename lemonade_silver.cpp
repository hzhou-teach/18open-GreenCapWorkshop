// Brian Lu
// 10 mins
// **********
// Sorting seemed to work I guess. /shrug
#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <limits>
#include <string>

bool sortBackwards(int a, int b) {
    return a > b;
}

int main()
{
    int N, temp;
    FILE *input = fopen("lemonade.in", "r");
    fscanf(input, "%d", &N);
    std::vector<int> cows;
    for (int i = 0; i < N; i++) {
        fscanf(input, "%d", &temp);
        cows.push_back(temp);
    }
    fclose(input);
    //ヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝ
    std::sort(cows.begin(), cows.end(), &sortBackwards);

    int cowcount = 0;
    for (int i = 0; i < N; i++) {
        if (cows[i] >= cowcount)
            cowcount++;
        else break;
    }
    //ヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝ
    FILE *output = fopen("lemonade.out", "w");
    fprintf(output, "%d\n", cowcount);
    fclose(output);

    return 0;
}